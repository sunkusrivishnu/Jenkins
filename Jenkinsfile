pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/sunkusrivishnu/Jenkins'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "./factorial.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
