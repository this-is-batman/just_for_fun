// this is the jenkins pipeline configuration for doing git checkout and then running the pytest for the testing modules
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/this-is-batman/just_for_fun.git']])
            }
        }
        stage('test') {
            steps {
                sh "python3 -m pytest"
            }
        }
    }
}