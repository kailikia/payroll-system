from peewee import *
try:
    db = PostgresqlDatabase('payrollsystem.db', user='postgres', password="1234", host="127.0.0.1")
    print("Successfully connected!")
except:
    print("Didn't connect!")


class Payroll(Model):
    id = IntegerField()
    payroll_date = DateField()
    overtime = FloatField()
    other_benefits = FloatField()
    nhif = FloatField()
    nssf = FloatField()
    payee = FloatField()
    employee_id = ForeignKeyField()


    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = "employees"

Payroll.create_table(fail_silently=True)