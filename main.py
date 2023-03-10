from fastapi import FastAPI
from database import database as connection

app = FastAPI(title='Project for learning python with fastapi',
              description = 'In this project you will find a set of configuration that I aply with fastapi',
              version=1
              )

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('DB connected')

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('DB connection stoped')

@app.get('/')
async def holamundo():
    return 'Hola Mundo'
