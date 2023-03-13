::@echo off
setlocal

set "url=%1"
set "nexus_credentials=%2"
set "nexus_credentials=%nexus_credentials%="
set "curl=C:\\Program Files\\Git\\mingw64\\bin\\curl.exe"

for %%i in ("%url%") do set "project_name=%%~nxsi"

curl -X "POST" "http://192.168.0.14:8081/service/rest/v1/blobstores/file" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Basic %nexus_credentials%" -H "NX-ANTI-CSRF-TOKEN: 0.8466380090355077" -H "X-Nexus-UI: true" -d "{\"path\": \"%project_name%\", \"name\": \"%project_name%\"}"

curl -X "POST" "http://192.168.0.14:8081/service/rest/v1/repositories/raw/hosted" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Basic %nexus_credentials%" -H "NX-ANTI-CSRF-TOKEN: 0.8466380090355077" -H "X-Nexus-UI: true" -d "{\"name\": \"%project_name%-Dev\", \"online\": true, \"storage\": {\"blobStoreName\": \"%project_name%\", \"strictContentTypeValidation\": true, \"writePolicy\": \"allow_once\"}, \"component\": {\"proprietaryComponents\": true}, \"raw\": {\"contentDisposition\": \"ATTACHMENT\"}}"

curl -X "POST" "http://192.168.0.14:8081/service/rest/v1/repositories/raw/hosted" -H "accept: application/json" -H "Content-Type: application/json" -H "Authorization: Basic %nexus_credentials%" -H "NX-ANTI-CSRF-TOKEN: 0.8466380090355077" -H "X-Nexus-UI: true" -d "{\"name\": \"%project_name%-Main\", \"online\": true, \"storage\": {\"blobStoreName\": \"%project_name%\", \"strictContentTypeValidation\": true, \"writePolicy\": \"allow_once\"}, \"component\": {\"proprietaryComponents\": true}, \"raw\": {\"contentDisposition\": \"ATTACHMENT\"}}"