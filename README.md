# Employee Management System - Django(Python)

Employee Management System built with Django framework and PostgreSQL database. This web application includes functionalities such as:

1. Login / Registration (Admin, Employee)
2. Add / Manage Employee (Admin)
3. Publish / Manage Notice (Admin)
4. Add / Manage Attendance (Admin)
5. Assign / Manage Work (Employee)
6. Send Request (Employee)
7. View Request, Notice, Works etc.

## Project Structure

The project has been optimized with an enhanced structure for better deployment and maintainability:

```
employee-management-django/
│
├── empmanagement/           # Main Django project directory
│   ├── accounts/            # User authentication app
│   ├── employee/            # Employee management app
│   ├── empmanagement/       # Project settings
│   ├── static/              # Static files
│   ├── templates/           # HTML templates
│   ├── .env                 # Local environment variables
│   └── manage.py            # Django management script
│
├── Procfile                 # Process file for deployment
├── render.yaml              # Render deployment configuration
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL

### Steps to Run Locally

1. Clone the repository to your local system
   ```bash
   git clone <repository-url>
   cd employee-management-django
   ```

2. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables
   - The project now uses a `.env` file in the empmanagement directory
   - You can modify the existing one or create your own with the following variables:
     ```
     SECRET_KEY=your_secret_key
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     DB_NAME=empdb
     DB_USER=postgres
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=5432
     ```

4. Make migrations and migrate
   ```bash
   cd empmanagement
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server
   ```bash
   python manage.py runserver
   ```

6. Access the application at http://127.0.0.1:8000/

## Screenshots

Login
![Login](https://github.com/omjogani/employee-management-django/blob/master/screenshots/Login.png "Login")

Dashboard
![Dashboard](https://github.com/omjogani/employee-management-django/blob/master/screenshots/Dashboard.png?raw=true "Dashboard")

Assign Work
![Assign Work](https://github.com/omjogani/employee-management-django/blob/master/screenshots/Assign%20Work.png?raw=true "Assign Work")

Notice
![Notice](https://github.com/omjogani/employee-management-django/blob/master/screenshots/Notice.png?raw=true "Notice")

Admin (Manage Employee)
![Admin (Manage Employee)](https://github.com/omjogani/employee-management-django/blob/master/screenshots/Admin%20Employee.png?raw=true "Admin (Manage Employee)")

### Check out more Screenshots in Screenshot Folder...

## Deployment on Render

This project is configured for easy deployment on Render.com:

1. Create a Render account at https://render.com

2. Connect your GitHub repository

3. Create a new web service:
   - Select your repository
   - Render will automatically detect the `render.yaml` configuration
   - Click "Apply"

4. The deployment will automatically:
   - Set up a PostgreSQL database
   - Install dependencies
   - Configure environment variables
   - Deploy your application

5. After deployment, your site will be available at `https://employee-management-system.onrender.com` (or a similar Render-assigned URL)

## Enhancements Made

1. **Project Structure**: Removed unused scripts and improved organization
2. **Environment Variables**: Added `.env` file support for secure configuration
3. **Deployment Config**: Added Render deployment configuration
4. **Static Files**: Improved static file handling with WhiteNoise
5. **Database Configuration**: Enhanced database setup for both local and production environments

>If you found this useful, make sure to give it a star 🌟

## Thank You!!
