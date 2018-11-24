from employee import Employee

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Employee.create(full_name='Peter Hillary',
    #                 kra_pin_number='11116',
    #                 department='Production',
    #                 position='Head of Productions',
    #                 basic_salary='245670',
    #                 house_allowance='494520')
    # # edwin = Employee.get(Employee.full_name == 'Edwin Martin')
    # print(edwin)
    # return 'edwin'
    allEmployees = Employee.select()
        # print(employee.full_name)

    return render_template("index.html", displayEmployees = allEmployees)

@app.route("/employee")
def employee():
    addEmployee = Employee.insert()
    return render_template("addEmployee.html", add_employee = addEmployee)



if __name__ == "__main__":
    app.run(debug=True, port=5005)