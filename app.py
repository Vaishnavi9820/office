import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
project_home = os.path.dirname(os.path.realpath(__file__))
sys.path.append(project_home)

# Add the Django project directory to the sys.path
django_project_dir = os.path.join(project_home, 'empmanagement')
sys.path.append(django_project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

# Print debugging information
print(f"Project home: {project_home}")
print(f"Django project directory: {django_project_dir}")
print(f"Current directory contents: {os.listdir(project_home)}")
print(f"Django project directory contents: {os.listdir(django_project_dir)}")
print(f"Python path: {sys.path}")

# Create the WSGI application
app = get_wsgi_application()
