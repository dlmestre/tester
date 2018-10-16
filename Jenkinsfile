pipeline {
	agent any
	stages {
		stage('Build docker images') {
			steps {
				echo 'Starting to build docker image'
				sh 'docker build -t tester:B${BUILD_NUMBER} .'
				sh 'docker run -it tester:B${BUILD_NUMBER}'
			}
		}
	}
}
