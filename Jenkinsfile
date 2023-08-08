pipeline {
    agent any

    environment {
        DOCKER_UNAME = "dhananjaypuri"
        DOCKER_PASS = credentials('docker_secret_pass')
        IMAGE_NAME = "${DOCKER_UNAME}/flaskapptest:${BUILD_ID}"
    }

    stages {
        stage('Code Checkout')
        {
            steps {
                echo "Code Checkout Stage Successfull"
            }
        }

        stage('Image Build Stage')

        {   

            steps {
                echo "Build Image: ${IMAGE_NAME}"
                sh '''
                echo "Cleaning Images"

                if docker rmi $(docker images | grep dhananjaypuri/flaskapptest | awk '{print $3}')
                then
                    echo "Images cleaned"
                fi
                echo ${DOCKER_PASS} | docker login -u ${DOCKER_UNAME} --password-stdin
                docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Image Push Stage')
        {
            input {
                ok "Yes, Push It !!"
                message "Should we continue?"
            }
            steps {
                echo "Pushing Image: ${IMAGE_NAME}"
                sh '''
                echo ${DOCKER_PASS} | docker login -u ${DOCKER_UNAME} --password-stdin
                docker image push ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        failure {
            echo "Build Failed"
        }
    }
}