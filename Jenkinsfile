pipeline {

    agent any

    environment {
        DOCKER_USERNAME    = "massire1"
        DOCKER_CREDENTIALS = credentials("my-docker-cred-id")
        IMAGE_VERSION      = "1.${BUILD_NUMBER}"
    }

    stages {
        // Étape 1 : Récupération du code source depuis GitHub
        stage("Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/massire1/testCICD.git'
            }
        }
         // Étape 2 : Exécution des tests
        stage("Test") {
            steps {
                echo "Tests en cours"
            }
        }
        stage("Build and Push Images") {
            steps {
                script {
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

        stage("Deploy with Docker Compose") {
            steps {
                script {
                    sh """
                    docker-compose down
                    docker-compose up -d --build
                    """
                }
            }
        }
    }
}