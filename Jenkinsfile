pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning Repo"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mehmoodharis74/MLOp_Tasks-2.git']])
            }
        }
        stage('Branch Name Check') {
            steps {
                echo 'Checking branch name'
                script {
                    def branchName = "${env.BRANCH_NAME}"
                    if (branchName == 'main')  {
                        echo "Branch Name: ${branchName}"
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                sh 'python --version'
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                sh 'python -m pytest test.py'
            }
        }
        
    }
}
