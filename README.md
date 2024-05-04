# Overview

In this project, we use GitHub to store source code for Flask web application.
Then use Github Actions to perform Continuous Integration
Integrate this project with Azure Pipeline to perform Continuous Delivery to Azure App Service

## Project Plan
Project Plan:
https://trello.com/b/ykSg6BZX/sprint-board-for-webapp
* A link to a Trello board for the project

  original project plan.xlsx 
  final project plan.xlsx
* A link to a spreadsheet that includes the original and final project plan>

## Instructions
![architecture](architecture.PNG?raw=true "architecture")
* Architectural Diagram (Shows how key parts of the system work)>


<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements
- Transform project to use microservice
- Add alert to the project

## Demo 

<TODO: Add link Screencast on YouTube>


