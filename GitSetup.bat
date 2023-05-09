@echo off
setlocal

set "url=%1"
set "folder=Assets"

::Extracting the project name from the URL.
for %%i in ("%url%") do set "project_name=%%~nxsi"

::Generating the ssh URL from the provided https URL
set ssh_url=%url:https://=git@%
set ssh_url=%ssh_url:.com/=.com:%

::Cloning the repository through ssh
git clone %ssh_url%
cd ./%project_name%

::Creating a branch to add the CI/CD files 
git checkout -b PipelineSetup

::Moving the needed file into the project repository
mv ../Resources/Jenkinsfile .

::Checking the existance of the Assets/Scripts/Editor path
::Creating the folders if they are not in the project
if not exist "%folder%" (
  echo Folder "%folder%" not found, wrong project structure.
  exit
) else (
  echo Folder "%folder%" found.
)

set "folder=Assets\Scripts"

if not exist "%folder%" (
  mkdir "%folder%"
  echo Folder "%folder%" created.
) else (
  echo Folder "%folder%" already exists.
)

set "folder=Assets\Scripts\Editor"

if not exist "%folder%" (
  mkdir "%folder%"
  echo Folder "%folder%" created.
) else (
  echo Folder "%folder%" already exists.
)

mv ../Resources/BuildUtility.cs ./Assets/Scripts/Editor

::Creating a commit on the branch with all the previous modifications
git add -A
git commit -m "Setup of the pipeline"
git push --set-upstream origin PipelineSetup
::You can now create a PR from GitHub