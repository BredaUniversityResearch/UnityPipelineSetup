import sys
import re

# Get command-line arguments
input_str = sys.argv[1]
jenkinsfile_path = sys.argv[2]

match = re.search(r"/(\w+)$", input_str)
if match:
    project_name = match.group(1)

# Read Jenkinsfile
with open(jenkinsfile_path, 'r') as f:
    jenkinsfile = f.read()

# Replace input string with "replaced-string"
modified_jenkinsfile = jenkinsfile.replace('PROJECT_NAME = ""', f'PROJECT_NAME = "{project_name}"')

# Write modified Jenkinsfile to new file
new_jenkinsfile_path = jenkinsfile_path.replace('JenkinsfileToFill', 'Jenkinsfile')
with open(new_jenkinsfile_path, 'w') as f:
    f.write(modified_jenkinsfile)