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
                bat "make install"
            }
        }
        stage('Testing') {
            steps {
                echo 'Running Tests'
                bat "make tests"
            }
        }
        stage('Branch Name Check') {
            steps {
                echo 'Checking branch name'
                script {
                    def branchName = env.BRANCH_NAME
                    if (branchName == 'main') {
                        echo "Branch Name: ${branchName}"
                    }
                }
            }
        }
    }
}
