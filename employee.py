from peewee import *
try:
    db = PostgresqlDatabase('payrollSystem', user='postgres', password="123456", host="127.0.0.1")
    print("Successfully connected!")
except:
    print("Didn't connect!")


class Employee(Model):
    full_name = CharField()
    kra_pin_number = CharField()
    department = CharField()
    position = CharField()
    basic_salary = FloatField()
    house_allowance = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = "employees"


Employee.create_table(fail_silently=True)