from peewee import *
from config import Settings

settings = Settings()

    

database = PostgresqlDatabase(
    settings.db_name,  
    user=settings.db_user, 
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port)