from datetime import date
import csv

class Location:
    def __init__(self, description, city, street, postal, country):
        self.description = description
        self.city = city
        self.street = street
        self.postal = postal
        self.country = country
    def print_to_string(self):
        print ("description: " + self.description + "\ncity: " + self.city + "\nstreet: " + self.street +
               "\npostal: " + self.postal + "\ncountry: " + self.country)

class Department:
    def __init__(self, description, id_manager):
        self.description = description
        self.id_manager = id_manager
    def print_to_string(self):
        print("description: " + self.description + "\nid_manager: " + self.id_manager)

class Grade:
    def __init__(self, description, min_salary, max_salary):
        self.description = description
        self.min_salary = min_salary
        self.max_salary = max_salary
    def print_to_string(self):
        print("description: " + self.description + "\nmin_salary: " + self.min_salary + "\nmax_salary: " +
              self.max_salary)

class Project:
    def __init__(self, description, client, monthly_cost, start_date, end_date, total_cost):
        self.description = description
        self.client = client
        self.monthly_cost = monthly_cost
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
    def print_to_string(self):
        print("description: " + self.description + "\nclient: " + self.client + "\nmonthly_cost: " + self.monthly_cost +
              "\nstart_date: " + self.start_date + "\nend_date: " + self.end_date + "\ntotal_cost: " + self.total_cost)

class Job:
    def __init__(self, description):
        self.description = description
    def print_to_string(self):
        print("description: " + self.description)

class Manager:
    def __init__(self, id_employee):
        self.id_employee = id_employee
    def print_to_string(self):
        print("employee_id: " + self.id_employee)

class Contract:
    def __init__(self, type, start_date, end_date, id_grade, salary_factor, id_employee):
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.id_grade = id_grade
        self.salary_factor = salary_factor
        self.id_employee = id_employee
    def print_to_string(self):
        print("type: " + self.type + "\nstart_date: " + self.start_date + "\nend_date: " + self.end_date +
              "\nid_grade: " + self.id_grade + "\nsalary_factor: " + self.salary_factor + "\nid_employee: " +
              self.id_employee)

class Employee:
    def __init__(self, first_name, last_name, email, phone_number, id_job, id_location, id_contract_active, id_manager,
                 id_department, id_grade, is_manager, is_officer, is_active, id_project_1, id_project_2, id_project_3,
                 id_project_4, id_project_5):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email + "@company.com"
        self.phone_number = phone_number
        self.id_job = id_job
        self.id_location = id_location
        self.id_contract_active = id_contract_active
        self.id_manager = id_manager
        self.id_department = id_department
        self.id_grade = id_grade
        self.is_manager = is_manager
        self.is_officer = is_officer
        self.is_active = is_active
        self.id_project_1 = id_project_1
        self.id_project_2 = id_project_2
        self.id_project_3 = id_project_3
        self.id_project_4 = id_project_4
        self.id_project_5 = id_project_5
    def print_to_string(self):
        print("first_name: " + self.first_name + "\nlast_name: " + self.last_name + "\nemail: " + self.email +
              "\nphone_number: " + self.phone_number + "\nid_job: " + self.id_job + "\nid_location: "
              + self.id_location + "\nid_contract_active: " + self.id_contract_active + "\nid_manager: " +
              self.id_manager +"\nid_department: " + self.id_department + "\nid_grade: " + self.id_grade +
              "\nis_manager: " + self.is_manager + "\nis_officer: " + self.is_officer + "\nis_active: " +
              self.is_active + "\nid_project_1: " + self.id_project_1 + "\nid_project_2: " + self.id_project_2 +
              "\nid_project_3: " + self.id_project_3 + "\nid_project_4: " +self.id_project_4 +
              "\nid_project_5: " + self.id_project_5)

def str_to_date(date):
    return "str_to_date('" + date + "', '%d.%m.%Y')"


list_of_locations = []
list_of_departments = []
list_of_grades = []
list_of_projects = []
list_of_jobs=[]
list_of_managers = []
list_of_contracts = []
list_of_employees= []

locations_insert_statements = []
departments_insert_statements = []
grades_insert_statements = []
projects_insert_statements = []
jobs_insert_statements = []
managers_insert_statements = []
contracts_insert_statements = []
employees_insert_statements = []

with open ('locations.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        record = Location(row[0], row[1], row[2], row[3], row[4])
        list_of_locations.append(record)

with open ('departments.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        record = Department(row[0], row[1])
        list_of_departments.append(record)

with open ('grades.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        record = Grade(row[0], row[1], row[2])
        list_of_grades.append(record)

with open ('projects.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        record = Project(row[0], row[1], row[2], row[3], row[4], row[5])
        list_of_projects.append(record)

with open ('jobs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        record = Job(row[0])
        list_of_jobs.append(record)

with open ('managers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        record = Manager(row[0])
        list_of_managers.append(record)

with open ('contracts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        record = Contract(row[0], row[1], row[2], row[3], row[4], row[5])
        list_of_contracts.append(record)

with open ('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        record = Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                          row[11], row[12], row[13], row[14], row[15], "", "")
        list_of_employees.append(record)

for location in list_of_locations:
    statement = "insert into locations(location_description, location_city, location_street, location_postal," \
                " location_country) values ('" + location.description + "','" + location.city + "','" + \
                location.street + "','" + location.postal + "','" + location.country + "');"
    locations_insert_statements.append(statement)

with open ("location_insert_statement.sql", "w") as output:
    for statement in locations_insert_statements:
        output.write(statement + "\n")

for department in list_of_departments:
    statement = "insert into departments(department_description, id_employee) values ('" + department.description + \
    "','" + department.id_manager + "');"
    departments_insert_statements.append(statement)

with open ("departments_insert_statements.sql", "w") as output:
    for statement in departments_insert_statements:
        output.write(statement + "\n")

for grade in list_of_grades:
    statement = "insert into grades(grade_description, grade_min_salary, grade_max_salary) values ('" + \
    grade.description + "','" + grade.min_salary + "','" + grade.max_salary + "');"
    grades_insert_statements.append(statement)

with open ("grades_insert_statements.sql", "w") as output:
    for statement in grades_insert_statements:
        output.write(statement + "\n")

for project in list_of_projects:
    statement = "insert into projects(project_description, project_client, project_monthly_cost, project_start_date," \
                " project_end_date, project_total_cost) values ('" + project.description + "','" + project.client + \
                "','" + project.monthly_cost + "'," + str_to_date(project.start_date) + \
               "," + str_to_date(project.end_date) +",'" + project.total_cost + "');"
    projects_insert_statements.append(statement)

with open ("projects_insert_statements.sql", "w") as output:
    for statement in projects_insert_statements:
        output.write(statement + "\n")

for job in  list_of_jobs:
    statement = "insert into jobs(job_description) values ('" + job.description + "');"
    jobs_insert_statements.append(statement)

with open ("jobs_insert_statements.sql", "w") as output:
    for statement in jobs_insert_statements:
        output.write(statement + "\n")

for manager in list_of_managers:
    statement = "insert into managers(id_employee) values ('" + manager.id_employee + "');"
    managers_insert_statements.append(statement)

with open ("managers_insert_statements.sql", "w") as output:
    for statement in managers_insert_statements:
        output.write(statement + "\n")

for contract in list_of_contracts:
    statement = "insert into contracts(contract_type, contract_start_date, contract_end_date, id_grade," \
                "contract_salary_factor, id_employee) values ('" + contract.type + "'," + \
                str_to_date(contract.start_date) + ","+ str_to_date(contract.end_date) + ",'" + \
                contract.id_grade + "','" + contract.id_employee + "');"
    contracts_insert_statements.append(statement)

with open ("contracts_insert_statements.sql", "w") as output:
    for statement in contracts_insert_statements:
        output.write(statement + "\n")

for employee in list_of_employees:
    statement = "insert into employees(employee_first_name, employee_last_name, employee_email, employee_phone_number" \
                ", id_job, id_location, id_contract_active, id_manager, id_department, id_grade, is_manager" \
                ", is_officer, is_active, id_project_1, id_project_2, id_project_3, id_project_4, id_project_5)" \
                "values ('" + employee.first_name + "','" + employee.last_name + "','" + employee.email + "','" + \
                employee.phone_number + "','" + employee.id_job + "','" + employee.id_location + "','" + \
                employee.id_contract_active + "','" + employee.id_manager + "','" + employee.id_department + "','" + \
                employee.id_grade + "','" + employee.is_manager + "','" + employee.is_officer + "','" + \
                employee.is_active + "','" + employee.id_project_1 + "','" + employee.id_project_2 + "','" + \
                employee.id_project_3 + "'," + "null" + "," + "null" + ");"
    employees_insert_statements.append(statement)

with open("employees_insert_statements.sql", "w") as output:
    for statement in employees_insert_statements:
        output.write(statement + "\n")


