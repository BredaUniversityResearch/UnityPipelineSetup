#!groovy

def COLOR_MAP = [
    'SUCCESS': 'good', 
    'FAILURE': 'danger',
]

parameters {
  string(name: 'GITHUB_REPO_NAME', description: 'Enter the HTTPS URL of the GitHub repository')
}

pipeline {
	environment {        		
		NEXUS_CREDENTIALS = credentials('NEXUS_CREDENTIALS')
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
					def githubRepoName = env.GITHUB_REPO_NAME
					withEnv(["REPO_NAME=${githubRepoName}"]) {
						bat '''NexusSetup.bat %REPO_NAME% %NEXUS_CREDENTIALS%'''
					}
				}
			}
		}
		stage('Jenkinsfile Creation') {
			steps {
				script {
					def githubRepoName = env.GITHUB_REPO_NAME
					withEnv(["REPO_NAME=${githubRepoName}"]) {
						bat '''py JenkinsFileSetup.py %REPO_NAME% ./Resources/JenkinsfileToFill'''
					}
				}
			}
		}
		stage('Push to Project') {
			steps {
				script {
					def githubRepoName = env.GITHUB_REPO_NAME
					withEnv(["REPO_NAME=${githubRepoName}"]) {
						bat '''GitSetup.bat %REPO_NAME%'''
					}
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
