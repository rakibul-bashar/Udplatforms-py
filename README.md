# Udplatforms api With Django 3 with python3

# Use Technologies below:

#Backend server

## All of the bellow technologies are used --

Django 3.1

djangorestframework

For ADMIN customization  used django-reversion libray

For API Documentation used Swagger libray (drf-yasg)

For Unit Test used Facker, Factory-boy libray`

# Run Django Applications

# Create Virtual environment 
python3 -m venv my-env

On Unix or MacOS, run:
source my-env/bin/activate

On Windows, run:
my-env\Scripts\activate.bat

# Install projects version dependencies:
pip install -r requirements.txt

# Run projects
python manage.py runserver

# For db migrations
python manage.py makemigrations

# For db invidiual app migrations
python manage.py makemigrations common users

# For db migrate
python manage.py migrate

# For Run Unit Tests
python src/manage.py test users.tests

# Swagger API Docs

When you run our application, specification will be generated. You can check it here:

### http://localhost:8000/swagger/
### http://localhost:8000/redoc/
### http://localhost:8000/swagger.json

# Screencast on our applications doc
<img src="images/Screenshot%20from%202020-08-22%2000-39-10.png">





