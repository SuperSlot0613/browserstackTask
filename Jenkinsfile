pipeline {
    agent any

    environment {
        IMAGE_NAME      = 'browserstacktask'
        CONTAINER_NAME  = 'browserstacktask_container'
        WORKDIR         = '/app' // adjust if your code lives somewhere else inside the image
        PATH            = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  echo "[INFO] Building Docker image..."
                  docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Run Tests in Docker Container') {
            steps {
                sh '''
                  echo "[INFO] Removing old container (if any)..."
                  docker rm -f ${CONTAINER_NAME} || true

                  echo "[INFO] Running tests inside container..."
                  mkdir -p allure-results

                  # run pytest with allure plugin inside container
                  docker run --name ${CONTAINER_NAME} \
                  -v pytest_code:/usr/local/lib/python3.11/site-packages \
                  -v webdriver_cache:/root/.wdm \
                  -v pytest_browser:/root/.cache/ms-playwright \
                  -v $(pwd)/allure-results:/app/allure-results \
                  --shm-size=2g \
                  ${IMAGE_NAME} \
                  pytest -v -s --alluredir=/app/allure-results || true
                  # The '|| true' ensures the stage completes even if tests fail, so Allure report still generated
                '''
            }
        }

        stage('Collect Allure Results') {
            steps {
                echo "[INFO] Archiving Allure results..."
                archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            }
        }

        stage('Allure Report') {
            steps {
                echo "[INFO] Generating Allure report in Jenkins..."
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo "[INFO] Cleaning up container..."
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
        success {
            echo "[INFO] Pipeline completed successfully."
        }
        failure {
            echo "[INFO] Tests failed but pipeline still processed Allure report."
        }
    }
}
