pipeline {
    agent any
    
    environment {
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials') // Use your Jenkins credentials ID here
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/vinaysunhare/indore-finance-service.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t indore-finance-service .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Use Jenkins environment variables for Docker Hub credentials
                    sh """
                        echo $DOCKER_CREDENTIALS_PSW | docker login -u $vinaysunhare --vinay2503-stdin
                        docker push indore-finance-service
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Deploy to Kubernetes logic goes here
            }
        }
    }
}
