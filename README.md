# tesa-project
Groovy Scm Pipeline , Ansible deploy a Docker , BASH script extract ++

## Jenkins Pipeline with Shared Libraries
### Features
- Triggered by SCM changes.
- Builds an artifact using a build script.
- Packages the artifact into a tarball.
- Uploads the packaged artifact to a repository.



## Flask App Deployment with Docker, Docker Compose, and Ansible
This project demonstrates how to deploy a simple Flask application with Docker, Docker Compose, and Ansible.

## Prerequisites
Ensure that the following software is installed on your machine:

- Docker: Install Docker
- Docker Compose: Install Docker Compose
- Ansible: Install Ansible
## Project Overview
- Flask Application: A simple Flask app that tracks page hits and stores them in a hits.json file.
- Dockerfile: Defines the image for the Flask app.
- Docker Compose: Simplifies running the Flask app and its dependencies in containers.
- Ansible: Automates the deployment process, including installing Docker, building the image, and running the containers.

## Project Structure

* ├── app.py                
* ├── Dockerfile            
* ├── docker-compose.yml   
* ├── requirements.txt     
* ├── ansible/              
* │   └── deploy.yaml       
* └── README.md           
## Step-by-Step Process

#### Clone the Repository 
 Clone this repository to your local machine:

`git clone <repo-url>`
`cd <repo-directory>`
#### Build and Push Docker Image
Before running the application, we need to build the Docker image and push it to Docker Hub.

##### Build the Docker Image Locally
Navigate to the directory containing the Dockerfile and build the image:

`docker build -t flask_app_image_name:latest`

Tag the Docker Image for Docker Hub
After building the image, tag it for your Docker Hub account:

docker tag flask_app_image_name:latest shlomiaz/flask_app_image_name:latest
Push the Docker Image to Docker Hub
Push the image to Docker Hub:

bash
Copy
Edit
docker push shlomiaz/flask_app_image_name:latest
Ensure you’re logged into Docker Hub using docker login before pushing.

3. Set Up and Run with Docker Compose
To start the Flask app and its associated database container, you can use Docker Compose.

Update docker-compose.yml
Ensure that the docker-compose.yml file is correctly set up to reference your image:

yaml
Copy
Edit
version: '3.8'

services:
  web:
    image: "shlomiaz/flask_app_image_name:latest"
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_PATH=/data/hits.json
    volumes:
      - app_data:/data

  db:
    image: alpine
    command: ["sh", "-c", "while true; do sleep 3600; done"]
    volumes:
      - app_data:/data

volumes:
  app_data:
    driver: local
Start the Services with Docker Compose
Run the Flask app and its database container using Docker Compose:

bash
Copy
Edit
docker-compose up -d
This will start the services in the background. You can visit http://localhost:5000 to access the Flask app.

4. Automate Deployment with Ansible
You can automate the entire process of deploying the Flask app using Ansible.

Install Ansible
If Ansible is not installed, you can install it via pip:

bash
Copy
Edit
pip install ansible
Update the Ansible Playbook
Ensure the deploy.yaml playbook references your Docker image and other configurations correctly.

Run the Ansible Playbook
To deploy the Flask app, run the Ansible playbook:

bash
Copy
Edit
ansible-playbook -K ansible/deploy.yaml
This will:

Install Docker and Docker Compose (if not installed).
Copy Flask app files to the target machine.
Build and start the Docker containers using Docker Compose.
5. Verify the Deployment
After running the playbook, you should be able to access the Flask app at http://localhost:5000. The page will display the number of hits the app
### requirements before deploy
- please maje sure that ansible-galaxy collection install community.docker installed 
- if deploy happened in wsl please make sure you have Docker Desktop 
- to 
