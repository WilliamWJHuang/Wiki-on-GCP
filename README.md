# Continuous Delivery of Flask Application on GCP: mini_wiki

## Goal
This project is developed for ECE590.24 with a view to demonstrate the ability to build a simple flask application hosted on Google Cloud Platform with continuous delivery capability.

## Description
This project is a mini wikipedia which returns you the company name, summary and the Wikipedia link in html format once you enter the company name on the url.

## Resources:
Website: https://gcpminiwiki.appspot.com
<br>Demo Video: 

## A Step-by-Step Tutorial
1. Create a new project on Google Cloud Platform
2. Activate Google Cloud Shell and Launch Editor
3. Set the shell to this project with the following command: gcloud config set project [PROJECT_ID]
4. Enable two APIs: Cloud Build & App Engine
5. Create a new Github Repo for this project
6. Go back to the Google Cloud Shell and use command ssh-keygen -t rsa to generate ssh keys, then access the key with the command: cat ~/.ssh/id_rsa.pub
7. Add the new ssh key at Github setting, the ssh key should start like "ssh-rsa AAAAB3NXXXXXXXXXXXXXXXX"
8. Git clone the repo at Google Cloud Shell
9. Add the files
- app.yaml: set the configuration of the infrastructure we are running on
- requirements.txt: specify the packages we need for this project
- Makefile: pipline for compilation
- main.py: the codes for the flask application
10. Create Google Application with the command: gcloud app create and specify your location
11. Create a virtual environment exclusively for this project with the command virtualenv --python $(which python) venv, you can activate the environment with source venv/bin/activate and use deactivate to deactivate the environment.
12. In the virtual environment, use make install to install the packages you need and specify in the requirements.txt
13. Test your application in local by the commaind python main.py
14. Deploy your application on Google Cloud Platform: gcloud app deploy
15. Use the command: gcloud app browse to get the url to view your site
16. git add., git commit and git push to make the Github repo up-to-date
17. To set continuous delivery, go to Cloud Build under the Tools section in Google Console
18. Add cloudbuild.yaml at the Cloud Shell under the project folder
19. Select Github as your source and follow the instruction to complete setup.
