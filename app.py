import os
import sys

# Print current working directory for debugging
print(f"Current working directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir('.')}")

# Add project root to path
root_path = os.path.dirname(os.path.abspath(__file__))
print(f"Root path: {root_path}")
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Add empmanagement directory to path
emp_path = os.path.join(root_path, 'empmanagement')
print(f"Empmanagement path: {emp_path}")
if emp_path not in sys.path:
    sys.path.insert(0, emp_path)

# Add inner empmanagement directory to path
inner_emp_path = os.path.join(emp_path, 'empmanagement')
print(f"Inner empmanagement path: {inner_emp_path}")
if inner_emp_path not in sys.path:
    sys.path.insert(0, inner_emp_path)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empmanagement.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
