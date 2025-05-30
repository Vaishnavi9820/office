import os
import sys

# Add the project directory to the path
project_home = os.path.dirname(os.path.realpath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to the Django project directory
os.chdir('empmanagement')

# Import the Django WSGI application
from empmanagement.wsgi import application as app
