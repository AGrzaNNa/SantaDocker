1. Install the required dependencies:

        pip install -r requirements.txt

2 Import Libraries

In your Python script (main.py or a similar file), ensure the following import statements are present at the beginning:

    from fastapi import FastAPI
    import sqlite3


3 Database Setup

The project uses SQLite as its database. 
The database file (database.db) is created automatically upon running the application for the first time.
Running the FastAPI Application

    Run the FastAPI application using the following command:
    uvicorn main:app --reload

After enter the generated localhost/link theres need to add /docs then u will be send to api web 

API Endpoints
Packages

    POST /package: Add a new package.
    PUT /package: Update the status of a package.
    GET /package: Retrieve information about a specific package.
    DELETE /package: Delete all delivered packages.

Elves

    POST /elfs: Add a new elf.
    PUT /elfs: Update the vacation and daternity status of an elf.
    GET /elfs: Retrieve information about a specific elf.
    DELETE /elfs: Fire an elf.

4 Create Docker Hub Account and Repository

 Docker Hub Account Creation:
        Visit Docker Hub in your web browser.
        Click on the "Sign Up" button to create a new account.
        Fill in the required information and follow the prompts to create your Docker Hub account.

 Create a New Repository:
        After logging in to your Docker Hub account, navigate to the "Repositories" tab.
        Click on the "Create Repository" button.
        Choose a name for your repository (e.g., <repository_name>).
        Add a description if desired.
        Set the visibility (public or private) according to your preferences.
        Click the "Create" button to create the new repository.

5 Docker Deployment

 Install Docker Desktop from https://www.docker.com/products/docker-desktop/.

After installation, run Docker Desktop. Restart your PC to ensure all changes take effect.

Log in to Docker Desktop with your account credentials.

Create a new container following the steps in the Docker Desktop interface. Execute the necessary commands.

Build the Docker image using PyCharm's Docker plugin or the command line:

bash

    docker build -t <image_name> .

Push the image to Docker Hub using PyCharm's Docker plugin or the command line:

bash

    docker login
    docker push <image_name>

    Access the API at http://127.0.0.1:8000.
