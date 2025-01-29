# Tesa-Project
1. Groovy Scm Pipeline 
2. Ansible deploy a Docker 
3. BASH script extract 
4. Deploy Artifact

## 1. Jenkins Pipeline with Shared Libraries (build an artifact folder)
### Pipeline Overview 
- **SCM Checkout**: Pulls the latest code from GitHub.
- **Environment** Preparation: Uses a shared library to configure SCM details.
- **Dependency Installation**: Installs Docker Compose, fixes APT sources, and ensures zip is installed.
- **Build & Package**: Uses docker-compose to build and package the app into a ZIP file.
- **Push to Git**: Commits and pushes changes back to GitHub.
- **Automated Execution**: Triggers every minute if there are new commits.
- **post block**: 
- On success: It prints a success message and triggers the deployment job (deploy-flask-project).
- On failure: It prints an error message, asking users to check the logs for more details.



## 2. Flask App Deployment with Docker, Docker Compose, and Ansible
This project demonstrates how to deploy a simple Flask application with Docker, Docker Compose, and Ansible.

### Prerequisites
Ensure that the following software is installed on your machine:
- Docker: Install Docker
- Docker Compose: Install Docker Compose
- Ansible: Install Ansible
### Project Overview
- **Flask Application**: A simple Flask app that tracks page hits and stores them in a hits.json file.
- **Dockerfile**: Defines the image for the Flask app.
- **Docker Compose**: Simplifies running the Flask app and its dependencies in containers.
- **Ansible**: Automates the deployment process, including installing Docker, building the image, and running the containers.

## Project Structure

* ├── app.py                
* ├── Dockerfile            
* ├── docker-compose.yml   
* ├── requirements.txt     
* ├── ansible/              
* │   └── deploy.yaml       
* └── README.md           

# 3. BASH script extract

The script takes files and directories as input and attempts to decompress them.
- **File supported**: It supports different compression formats
including:
Gzip (.gz)
Bzip2 (.bz2)
Zip (.zip)
Compress (.Z)
- **Recursively**: the script can recursively extract archives from directories if the -r flag is used.
- **Flags**: the script provides verbose output when the -v flag is used.
- **Help** for main help menu use (-h).

# 4. Deploy Artifact 

### Pipeline Overview

This Groovy script is called from the first pipeline, named deploy-flask-project, and it automates the following process:

- Clone out code from SCM.
- Ensuring Docker is installed, and installing it if necessary.
- Installing Docker Compose.
- Finding and extracting a ZIP artifact using an section 3 (BASH script extract).
- Deploying the artifact uploaded in section 1 (Jenkins Pipeline with Shared Libraries) using an Ansible playbook from section 2 (Flask App Deployment with Docker, Docker Compose, and Ansible) to the deployments.