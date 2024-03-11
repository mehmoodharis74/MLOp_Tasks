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
                script {
                    // Use pip3 on Unix-like systems and pip on Windows
                    def pipCommand = isUnix() ? 'pip3' : 'pip'
                    sh "${pipCommand} install -r requirements.txt"
                }
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                // Use python3 on Unix-like systems and python on Windows
                def pythonCommand = isUnix() ? 'python3' : 'python'
                sh "${pythonCommand} -m pytest test.py"
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
    }
}
