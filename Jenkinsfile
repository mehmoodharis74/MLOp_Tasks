pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning Repo"
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/mehmoodharis74/MLOp_Tasks-2.git']])
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                    sh 'python3 -m install -r requirements.txt'
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                 sh 'python3 -m pytest test.py'
            }
        }
        stage('Branch Name Check') {
            steps {
                echo 'Checking branch name'
                script {
                    def branchName = "${env.GIT_BRANCH}"
                    if (branchName == 'main')  {
                        echo "Branch Name: ${branchName}"
                    }
                }
            }
        }
    }
}
