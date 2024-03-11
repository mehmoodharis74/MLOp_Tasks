pipeline {
    agent {
        label 'ubuntu-latest'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                echo 'Checking out the repository'
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python'
                script {
                    // Replace '3.12.0' with the desired Python version
                    tool 'Python 3.12.0'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                script {
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Tests'
                script {
                    sh 'pytest test.py'
                }
            }
        }
    }
}
