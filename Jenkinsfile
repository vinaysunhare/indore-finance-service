pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/vinaysunhare/indore-finance-service.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t indore-finance-service:latest .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Use hardcoded Docker credentials for login and push
                    sh """
                        echo vinay2503 | docker login -u vinaysunhare123@gmail.com --password-stdin
                        docker push indore-finance-service:latest
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
