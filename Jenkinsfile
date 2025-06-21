pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Build containers') {
            steps {
                sh 'docker compose -f $COMPOSE_FILE build'
            }
        }

        stage('Start system') {
            steps {
                sh 'docker compose -f $COMPOSE_FILE up -d'
                sh 'sleep 10' // περιμένουμε λίγο για να ξεκινήσει
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking if web service is healthy...'
                sh 'curl -f http://web:5000/users'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker compose -f $COMPOSE_FILE down'
        }
    }
}
