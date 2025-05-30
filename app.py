import os
import sys
import importlib.util

# Get the project root directory
project_home = os.path.dirname(os.path.realpath(__file__))

# Add project directory to Python path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Add empmanagement directory to Python path
empmanagement_path = os.path.join(project_home, 'empmanagement')
if empmanagement_path not in sys.path:
    sys.path.insert(0, empmanagement_path)

# Print debugging information (helpful for debugging deployment issues)
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Project directory: {project_home}")
print(f"Python path: {sys.path}")
print(f"Directory contents: {os.listdir(project_home)}")
print(f"Empmanagement directory contents: {os.listdir(empmanagement_path)}")

# Define the WSGI application directly
def create_wsgi_app():
    """Create a WSGI application for Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')
    from django.core.wsgi import get_wsgi_application
    return get_wsgi_application()

# This is what Gunicorn will use
app = create_wsgi_app()
