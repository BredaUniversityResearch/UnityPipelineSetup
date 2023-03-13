@echo off
setlocal

set "url=%1"

::Extracting the project name from the URL.
for %%i in ("%url%") do set "project_name=%%~nxsi"

::Generating the ssh URL from the provided https URL
set ssh_url=%url:https://=git@%
set ssh_url=%ssh_url:.com/=.com:%

git clone %ssh_url%
cd ./%project_name%
git checkout -b PipelineSetup
mv ../Resources/Jenkinsfile .
mv ../Resources/BuildUtility.cs ./Assets/Scripts
git add -A
git commit -m "Setup of the pipeline"
git push --set-upstream origin PipelineSetup