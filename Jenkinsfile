pipeline {
    agent any

    stages {
        stage('Build containers') {
            steps {
                sh 'docker compose -f docker-compose.yml build'
            }
        }

        stage('Start system') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d'
                sh 'sleep 10'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking if web service is healthy...'
                sh 'docker compose exec -T web curl -f http://localhost:5000/users'

            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'docker compose exec -T web pytest tests/'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker compose -f docker-compose.yml down'
        }
    }
}
