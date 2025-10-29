pipeline {
  agent any

  environment {
    IMAGE_NAME = "scizor27/chatbot-demo/chatbot-demo"
    IMAGE_TAG = "${env.BUILD_ID}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Unit Tests') {
      steps {
        dir('chatbot') {
          sh 'python -m pip install --upgrade pip'
          sh 'pip install -r requirements.txt'
          sh 'pytest -q'
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dir('chatbot') {
            sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
          }
        }
      }
    }

    stage('Push Image') {
      steps {
        // Requires Docker Hub credentials configured in Jenkins (username/password)
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
          sh "echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin"
          sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
        }
      }
    }

    stage('Deploy (local docker-compose)') {
      steps {
        // For demo we redeploy local docker-compose: stop existing, set new image and up
        sh 'docker-compose down || true'
        sh 'docker-compose build chatbot'
        sh 'docker-compose up -d --no-deps chatbot'
      }
    }
  }

  post {
    always {
      echo "Build finished: ${currentBuild.fullDisplayName}"
    }
    success {
      echo "SUCCESS: ${env.BUILD_URL}"
    }
    failure {
      echo "FAILED: ${env.BUILD_URL}"
    }
  }
}
