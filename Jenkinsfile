#!groovy

def COLOR_MAP = [
    'SUCCESS': 'good', 
    'FAILURE': 'danger',
]

pipeline {
	environment {        		
		NEXUS_CREDENTIALS = credentials('NEXUS_CREDENTIALS')
		GITHUB_REPO_NAME = ${params.GITHUB_REPO_NAME}
		WINDOWS_BUILD = ${params.WINDOWS_BUILD}
		MACOS_BUILD = ${params.MACOS_BUILD}
		ANDROID_BUILD = ${params.ANDROID_BUILD}
		IOS_BUILD = ${params.UNITY_VERSION}
    }

	agent {
        node {
        	label 'windows'
		}
	}
	
	stages {
        stage('Clone Script') {
           	steps {
               	checkout scm
			}
		}
		stage('Nexus Setup') {
			steps {				
				script {
					bat '''NexusSetup.bat ${params.GITHUB_REPO_NAME} %NEXUS_CREDENTIALS%'''
				}
			}
		}
		stage('Jenkinsfile Creation') {
			steps {
				script {
					bat '''py JenkinsFileSetup.py %GITHUB_REPO_NAME% ./Resources/JenkinsfileToFill %WINDOWS_BUILD% %MACOS_BUILD% %ANDROID_BUILD% %IOS_BUILD% %UNITY_VERSION%'''
				}
			}
		}
		stage('Push to Project') {
			steps {
				script {
					bat '''GitSetup.bat %GITHUB_REPO_NAME%'''
				}
			}
		}
	}		
	post {
		always {				
			slackSend color: COLOR_MAP[currentBuild.currentResult],
			message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}"
		}
	}
}
