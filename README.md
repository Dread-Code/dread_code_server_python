# dread_code_server_python

My first server API with python

## Prerequisites

* Python 3.10 for run this project. I suggest use pyenv for this.
* Docker compose

## Steps to run this server

1. Run the DB:
 ```
 docker compose up
 ```
 
 2. Run the server
 ```
 uvicorn main:app --reload
 ```
