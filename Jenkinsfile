pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vinaysunhare/indore-finance-service.git'
            }
        }
        stage('Build with Maven') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Docker Build and Push') {
            steps {
                sh '''
                IMAGE_NAME=indore-finance-service
                TAG=latest
                DOCKER_REGISTRY=your-docker-registry-url

                docker build -t $DOCKER_REGISTRY/$IMAGE_NAME:$TAG .
                docker push $DOCKER_REGISTRY/$IMAGE_NAME:$TAG
                '''
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                IMAGE_NAME=indore-finance-service
                TAG=latest
                DOCKER_REGISTRY=your-docker-registry-url
                KUBE_NAMESPACE=default

                kubectl set image deployment/indore-finance-service indore-finance-service=$DOCKER_REGISTRY/$IMAGE_NAME:$TAG -n $KUBE_NAMESPACE
                kubectl rollout status deployment/indore-finance-service -n $KUBE_NAMESPACE
                '''
            }
        }
    }
}
