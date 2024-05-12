# Machine Learning API with FastAPI

Welcome to the Machine Learning API repository built with FastAPI! This repository contains code to deploy machine learning models as APIs using the FastAPI framework, a modern and high-performance web framework for building APIs with Python.

## Demo
Check out the live demo of the API: [API Demo](https://facemask-detection-iz4mp5mymq-uc.a.run.app/docs)

## Deployment on Google Cloud Platform (GCP)
To deploy this API on Google Cloud Platform, Google Cloud Run service is used to achieve scalable and reliable hosting.


## Overview
This API serves as a bridge between machine learning models and applications, allowing users to interact with models through simple HTTP requests. Whether you're deploying models for predictions, classification, object detection, or any other task, this API provides a scalable and efficient solution.

Please note that the samples provided in this repository specifically focus on object detection tasks. The API supports the integration of object detection models, enabling real-time analysis of images.


 ⚠️ **Disclaimer:** This repository is intended solely for the purpose of testing and evaluation in alignment with the requirements for the AI Engineer job position. Deploying machine learning models in a public environment may expose sensitive data and pose security risks. 

## Features
- **FastAPI Integration:** Utilizes FastAPI framework for building robust and high-performance APIs.
- **Model Deployment:** Deploy machine learning models seamlessly as APIs.
- **Swagger Documentation:** Automatically generates interactive API documentation with Swagger UI for easy exploration.
- **Input Validation:** Ensures data integrity with input validation.

## Quick Start (Running Locally)
1. Clone this repository:
   ```bash
   git clone https://github.com/dinosptr/facemask-api.git
   
2. Navigate to Cloned Directory:
    ```bash
    cd facemask-api

3. Install dependencies:
    ```bash
   pip install -r requirements.txt
4. Run the FastAPI server:
    ```bash
    python main.py
5. Access the API documentation:
Open your web browser and go to http://localhost:8000/docs to explore the interactive API documentation provided by Swagger UI.


## Author
[Achmad Dino Saputra](https://www.linkedin.com/in/achmad-dino-saputra/)
