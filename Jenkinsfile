pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage('Build Flask App') {
            steps {
                script {
                    sh 'docker-compose build web'
                }
            }
        }

        stage('Start Containers') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'sleep 10 && curl -f http://localhost:5000/users || exit 1'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker-compose down'
            }
        }
    }
}
