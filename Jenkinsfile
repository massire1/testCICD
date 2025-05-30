pipeline {
    agent any

    environment {
        DOCKER_USERNAME    = 'massire1'
        DOCKER_CREDENTIALS = credentials('my-docker-cred-id')
        IMAGE_VERSION      = "1.${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'compose', url: 'https://github.com/massire1/testCICD.git'
            }
        }

        stage('Build and Push Images') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        // Backend
                        sh "docker build -t $DOCKER_USERNAME/testcicd-backend:$IMAGE_VERSION ./backend"
                        sh "docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}"
                        sh "docker push $DOCKER_USERNAME/testcicd-backend:$IMAGE_VERSION"

                        // Frontend
                        sh "docker build -t $DOCKER_USERNAME/testcicd-frontend:$IMAGE_VERSION ./frontend"
                        sh "docker push $DOCKER_USERNAME/testcicd-frontend:$IMAGE_VERSION"
                    }
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        //sh 'pwd'
                        //sh 'ls -la'
                        sh 'docker-compose down'
                        sh 'docker-compose up -d'
                    }
                }
            }
        }
    }
}