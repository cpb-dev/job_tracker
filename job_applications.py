#TEMPORARY PROJECT
#Used to collect information about jobs applied to and how many applications have been sent

import csv
import pandas

df = pandas.read_csv('job_applications.csv', index_col='company', parse_dates=['date_applied'])

def read_applications():
    print(df)

def new_application(company, role, date):
    with open('job_applications.csv', mode='w') as job_application:
        application_writer = csv.writer(job_application, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        application_writer.writerow([company, role, date])

def search_roles(role):
    result = df.loc[df['role'] == role]
    print(result)
    