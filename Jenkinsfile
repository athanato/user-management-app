pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "userapp"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/athanato/user-management-app.git'
            }
        }

        stage('Build containers') {
            steps {
                sh 'docker-compose -f docker-compose.yml build'
            }
        }

        stage('Start system') {
            steps {
                sh 'docker-compose -f docker-compose.yml up -d'
                sh 'sleep 10' // περιμένουμε τα services να σηκωθούν
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl -f http://localhost:5000/users || exit 1'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker-compose -f docker-compose.yml down'
        }
    }
}
