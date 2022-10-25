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
        application_writer = csv.DictWriter(job_application, fieldnames = field_names)

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

#Program

print("Welcome to the job application bot!")
print("Here I save the jobs you've applied to.")

u_inp = input(
    "What would you like to do today? \n Type the number of the option you want! \n 1. New Job Application \n 2. View all Applications \n 3. Search Applications \n Choice: "
)

if(u_inp == "1"):
    job_application()
elif(u_inp == "2"):
    read_applications()
elif(u_inp == "3"):
    search = input(
        "What would you like to search by? \n 1. Job Role \n 2. Company \n Choice: "
    )
    if(search == "1"):
        role = input("What role are you looking for?: ")
        search_roles(role)

    elif(search == "2"):
        company = input("What company are you looking for?: ")
        search_company(company)
