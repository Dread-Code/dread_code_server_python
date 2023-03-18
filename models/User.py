from peewee import *
from datetime import datetime
from database import database


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        database = database
        table_name = 'users'