pipeline {
	agent any
	stages {
		stage('Build docker images') {
			steps {
				echo 'Starting to build docker image'

                script {
                        def customImage = docker.build("tester:${env.BUILD_ID}")
                        customImage.push()
                    }
			}
		}
	}
}
