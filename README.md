Image Processing Application - Azure Functions
This repository contains the code and resources for an image processing application deployed using Azure Functions. The project is part of an MSc course and demonstrates how to build and deploy serverless image processing functions on Azure.

Repository Structure
Files and Directories
.vscode/:

Contains Visual Studio Code configuration files. These files help set up the development environment with the necessary settings and extensions for working on the project.
.funcignore:

Specifies files and directories that should be ignored by the Azure Functions CLI when deploying the function app. This file is used to exclude unnecessary files from being uploaded to the cloud.
.gitignore:

Specifies files and directories that should be ignored by Git. This ensures that temporary files, dependencies, and other non-essential files are not included in version control.
23.08.2024_18.50.59_REC-Image-Pro.mp4:

A video file that likely contains a demonstration or walkthrough of the image processing application. This could include an explanation of the code, deployment process, and live demonstration of the application's functionality.
function_app.py:

The main Python script that defines the Azure Function for image processing. This script contains the logic for processing images, such as resizing, filtering, or format conversion. The function is triggered by events (like an HTTP request) and performs the specified image processing tasks.
host.json:

A configuration file for Azure Functions that specifies runtime settings such as logging, timeouts, and other operational parameters. This file is essential for controlling how the function behaves in the Azure environment.
requirements.txt:

Lists the Python dependencies required for the project. This file ensures that all necessary libraries (e.g., for image processing or handling Azure services) are installed when the function app is deployed or run locally.
Purpose and Applications
This project showcases how to leverage Azure Functions for serverless image processing. Serverless computing allows you to deploy functions that automatically scale based on demand without managing the underlying infrastructure. This is particularly useful for image processing tasks that can vary greatly in complexity and resource requirements.

Key Features
Serverless Image Processing:

The application processes images in a serverless environment, making it scalable and cost-effective. The processing tasks could include resizing, cropping, filtering, and converting image formats.
Azure Functions:

The project uses Azure Functions to host and execute the image processing logic. Azure Functions provide a fully managed platform that automatically handles the infrastructure, scaling, and reliability.
Ease of Deployment:

