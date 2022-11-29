pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/jainavsanghvi10/Assignment_Jenkins_SE.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Palindrome.py"
                sh "./Palindrome.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_test_1.py"
                sh "./unit_test_1.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_test_2.py"
                sh "./unit_test_2.py"
            }
        }
    } 
}
