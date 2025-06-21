pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "user-management-app"
    }

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
                // Retry block: 5 προσπάθειες, με αναμονή 5 δευτερόλεπτα η κάθε μία
                script {
                    def retries = 5
                    def waitTime = 5
                    def success = false
                    for (int i = 0; i < retries; i++) {
                        def result = sh(
                            script: 'docker compose exec -T web curl -sf http://localhost:5000/users',
                            returnStatus: true
                        )
                        if (result == 0) {
                            success = true
                            break
                        } else {
                            echo "Service not ready yet. Retrying in ${waitTime}s..."
                            sleep(waitTime)
                        }
                    }
                    if (!success) {
                        error("Health check failed after ${retries} retries.")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
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
