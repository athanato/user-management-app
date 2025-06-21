pipeline {
    agent any

    stages {
        stage('Build containers') {
            steps {
                sh 'docker compose -f docker-compose.ci.yml build'
            }
        }

        stage('Start system') {
            steps {
                sh 'docker compose -f docker-compose.ci.yml up -d'
                sh 'sleep 10'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking if web service is healthy...'
                sh 'curl -f http://localhost:5000/users || exit 1'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker compose -f docker-compose.ci.yml down'
        }
    }
}
