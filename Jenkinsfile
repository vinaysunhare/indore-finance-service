pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vinaysunhare/indore-finance-service:latest'
        DOCKER_CLI_EXPERIMENTAL = 'enabled'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the latest code from GitHub
                git 'https://github.com/vinaysunhare/indore-finance-service.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t indore-finance-service .'
                }
            }
        }
        
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    sh 'echo $vinay2503 | docker login -u $vinaysunhare --password-stdin'
                    // Push the Docker image
                    sh 'docker push $vinaysunhare/indore-finance-service:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Assuming Kubernetes is set up, you can use kubectl to deploy the Docker image
                    sh '''
                        kubectl set image deployment/indore-finance-deployment indore-finance-service
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after job completes
        }
    }
}
