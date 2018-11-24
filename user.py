from employee import db
from peewee import  *

class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    class Meta:
        database = db
        table_name = "users"

User.create_table(fail_silently=True)

