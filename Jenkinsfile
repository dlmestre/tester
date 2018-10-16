pipeline {
	agent any
	stages {
		stage('Build docker images') {
			steps {
				echo 'Starting to build docker image'
				sh 'docker build -t tester:${env.BUILD_ID} .'
				sh 'docker run -d tester:${env.BUILD_ID}'
			}
		}
	}
}
