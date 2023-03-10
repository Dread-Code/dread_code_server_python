# dread_code_server_python

My first server API with python

## Prerequisites

* Python 3.10 for run this project. I suggest use pyenv for this.
* Docker compose

## Steps to run this server

1. Run the DB:
 ```
 docker compose up postgres
 ```
 
 2. Run the server
 ```
 docker compose up dreadcode_api
 ```

 Note: For some strange reason docker-compose in Mac doesn't load
 the container in order to depends_on property
