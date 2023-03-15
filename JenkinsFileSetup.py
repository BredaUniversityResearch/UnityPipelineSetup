import sys
import re

# Get command-line arguments
project_name = sys.argv[1]
jenkinsfile_path = sys.argv[2]
win_build = sys.argv[3]
mac_build = sys.argv[4]
android_build = sys.argv[5]
ios_build = sys.argv[6]
input_unity_version = sys.argv[7]
old_unity_version = "UNITY_EXECUTABLE = \"C:\\\\Program Files\\\\Unity\\\\Hub\\\\Editor\\\\2020.3.31f1\\\\Editor\\\\Unity.exe\""

with open("pr_template", 'r') as f:
    pr_template = f.read()
    
with open("dev_template", 'r') as f:
    dev_template = f.read()
    
with open("main_template", 'r') as f:
    main_template = f.read()

match = re.search(r"/(\w+)$", project_name)
if match:
    project_name = match.group(1)

# Read Jenkinsfile
with open(jenkinsfile_path, 'r') as f:
    jenkinsfile = f.read()


def change_build(previousBuild, newBuild, pr_template, dev_template, main_template):
    pr_template = re.sub(r'{}'.format(previousBuild), newBuild, pr_template)
    dev_template = re.sub(r'{}'.format(previousBuild), newBuild, dev_template)
    main_template = re.sub(r'{}'.format(previousBuild), newBuild, main_template)

    previousBuild = previousBuild.upper()
    newBuild = newBuild.upper()

    pr_template = re.sub(r'{}'.format(previousBuild), newBuild, pr_template)
    dev_template = re.sub(r'{}'.format(previousBuild), newBuild, dev_template)
    main_template = re.sub(r'{}'.format(previousBuild), newBuild, main_template)

    return pr_template, dev_template, main_template

# Replace input string with "project_name"
modified_jenkinsfile = jenkinsfile.replace('PROJECT_NAME = ""', f'PROJECT_NAME = "{project_name}"')

if(win_build):
    modified_jenkinsfile = modified_jenkinsfile.replace('//WINDOWSPR', pr_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//WINDOWSDEV', dev_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//WINDOWSMAIN', main_template)
    
pr_template, dev_template, main_template = change_build('Windows', 'MacOS', pr_template, dev_template, main_template)

if(mac_build):
    modified_jenkinsfile = modified_jenkinsfile.replace('//MACOSPR', pr_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//MACOSDEV', dev_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//MACOSMAIN', main_template)
    
pr_template, dev_template, main_template = change_build('MacOS', 'Android', pr_template, dev_template, main_template)

if(android_build):
    modified_jenkinsfile = modified_jenkinsfile.replace('//ANDROIDPR', pr_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//ANDROIDDEV', dev_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//ANDROIDMAIN', main_template)

pr_template, dev_template, main_template = change_build('Android', 'Ios', pr_template, dev_template, main_template)

if(ios_build):
    modified_jenkinsfile = modified_jenkinsfile.replace('//IOSPR', pr_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//IOSDEV', dev_template)
    modified_jenkinsfile = modified_jenkinsfile.replace('//IOSMAIN', main_template)

unity_version = old_unity_version.replace("2020.3.31f1", input_unity_version)
modified_jenkinsfile = modified_jenkinsfile.replace(old_unity_version, unity_version)

# Write modified Jenkinsfile to new file
new_jenkinsfile_path = jenkinsfile_path.replace('JenkinsfileToFill', 'Jenkinsfile')
with open(new_jenkinsfile_path, 'w') as f:
    f.write(modified_jenkinsfile)