#TEMPORARY PROJECT
#Used to collect information about jobs applied to and how many applications have been sent

import csv
import pandas
from datetime import date

today = date.today()

#Where to save the job applications
field_names = ['company', 'role', 'date_applied']
df = pandas.read_csv('job_application.csv', index_col='company')

def read_applications():
    print(df)

def new_application(company, role, date):
    with open('job_application.csv', mode='a') as job_application:
        application_writer = csv.DictWriter(job_application, fieldnames= field_names)

        application_writer.writerow({'company': company, 'role': role, 'date_applied': date})

def search_roles(role):
    result = df.loc[df['role'] == role]
    print(result)

def search_company(company):
    result = df.loc[df['company'] == company]
    print(result)

def job_application():
    inp_comp = input("What company have you applied for? \n")
    inp_role = input("What role was it for? \n")
    date = today.strftime("%d/%m/%Y")

    new_application(inp_comp, inp_role, date)

job_application()
    
