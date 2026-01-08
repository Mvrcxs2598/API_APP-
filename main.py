


# Initialize
"""
Setting up Django framework:
/django-admin startproject config .
Djange-admin is a cmd tool to fully use Django
Django creates a project skeleton once called (startproject)
Config is the name of the project package. "." is added to create in current directory.
Creates the Manage.py script - Creates the Operating system for running backend service
- config folder allows for configurations
- top-level URl router and
- entry points for deployment servers.
"""

"""
/python manage.py startapp api
Executes the manage.py and runs the app called "api"
- views: functions/classes requests
- models: database tables
- admin: admin site
- apps: configuartion for the app
- tests: tests for the app
Generally the app is a module and one project can host multiple apps. 

"""

"""
inside of api folder, we modify views.py to add in a function called health. 
health returns a status of type of Jsonresponse(similar to a dict). 

"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
