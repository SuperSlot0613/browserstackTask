pipeline {
    agent any

    environment {
        IMAGE_NAME = 'BowserStackTask'
        CONTAINER_NAME = 'BowserStackTask_container'
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Run Tests in Docker Container') {
            steps {
                sh '''
                  # Remove old container if exists
                  docker rm -f ${CONTAINER_NAME} || true

                  # Run container with volume mounts
                  docker run --name ${CONTAINER_NAME} \
                    -p 8081:8080 -p 50000:50000 \
                    -v python_deps:/usr/local/lib/python3.11/site-packages \
                    -v playwright_browsers:/root/.cache/ms-playwright \
                    ${IMAGE_NAME} \
                '''
            }
        }

        stage('Collect Allure Results') {
            steps {
                // Archive allure results for Jenkins Allure plugin
                archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            // Cleanup container after run
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
    }
}
