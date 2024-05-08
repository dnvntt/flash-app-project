# Overview

In this project, we use GitHub to store source code for Flask web application.
Then use Github Actions to perform Continuous Integration
Integrate this project with Azure Pipeline to perform Continuous Delivery to Azure App Service

## Project Plan
Project Plan:
https://trello.com/b/ykSg6BZX/sprint-board-for-webapp
* A link to a Trello board for the project

original project plan.xlsx  ![original project plan](original%20project%20plan.xlsx?raw=true "original project plan")

final project plan.xlsx ![final project plan](final%20project%20plan.xlsx?raw=true "final project plan")
* A link to a spreadsheet that includes the original and final project plan>

## Instructions
![architecture](architecture.PNG?raw=true "architecture")
* Architectural Diagram (Shows how key parts of the system work)>


<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project cloned into Azure Cloud Shell
  create ssh key in Azure cloud shell
ssh-keygen -t rsa -b 2048 -C "dvkhanhvn@gmail.com"

add ssh key to to github's key https://github.com/settings/keys
run command below to get content of ssh key and copy to github

cat .ssh/id_rsa.pub

  Using the command below to clone project from github
  
git clone git@github.com:dnvntt/flask-app-project.git
![ProjectCloned](ProjectCloned.PNG?raw=true "ProjectCloned")

* Passing tests that are displayed after running the `make all` command from the `Makefile`
# Create the Python Virtual Environment

python3 -m venv ~/.myrepo

source ~/.myrepo/bin/activate

# Local Test
Run "Make all" on Azure cloud shell to see the result
![make_all](make_all.PNG?raw=true "make_all")

* Output of a test run
Run application:

  export FLASK_APP=app.py
  
  flask run

![test_run](test_run.PNG?raw=true "test_run")

Github Actions CI

![github action](githubAction.PNG?raw=true "github action")

* Project running on Azure App Service
> To deploy Azure webapp using the command below:
> 
az webapp up -n flask-app-khanh --resource-group Azuredevops --sku FREE

![webApp](webApp.png?raw=true "webApp")

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

Step 1: in https://dev.azure.com/ create new project

Step 2: in project settings, create Service connections

Step 3: in project settings, create Agent pools => self hosted agent pool 

Step 4: Create new pipeline to automatic run CICD

In Azure Cloud:

Create virtual machine Ubuntu in Azure cloud to make it as devops agent

Azure Pipeline build and deploy successfull
![cicd](cicd.PNG?raw=true "cicd")

Load test using Locust

![locust](locust.PNG?raw=true "locust")
   
* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![make_predict_azure_app](make_predict_azure_app.png?raw=true "make_predict_azure_app")

* Output of streamed log files from deployed application
  
az webapp log tail --name flask-app-khanh --resource-group  Azuredevops

![streamed log](logStream.PNG?raw=true "streamed log")

## Enhancements
- Transform project to use microservice
- Add alert to the project

## Demo 

Step 1: Working Azure Cloud Shell environment for Continuous Integration  (timestamp:00:15)

Step 2: Github Action.  (timestamp:01:00)

Step 3: Azure pipeline.  (timestamp:01:20)

Step 4: Deploy Azure Web app   (timestamp:01:45)

Step 5: Successful deployment using Continuous Delivery on the Azure platform, including lint.  (timestamp:02:00)

Step 5: Successful machine learning prediction that returns back a JSON payload. (timestamp:02:50)

[![Watch the video](https://img.youtube.com/vi/lGrYL5Lqll8/hqdefault.jpg)](https://youtu.be/lGrYL5Lqll8)
 





