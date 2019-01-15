pipeline {
	agent any
	stages {
		stage('Build docker images') {
			steps {
			    sh 'pip install --user -r requirements.txt'
				echo 'Starting to build docker image'
				sh 'docker build -t tester:B${BUILD_NUMBER} .'
				sh 'docker run -i tester:B${BUILD_NUMBER}'
			}
		}
	}
}
