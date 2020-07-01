To run locally, do the usual:

# Create a Python 3.5 virtualenv

# Install dependencies:

    pip install -r requirements.txt
    
# Create tables:
    python manage.py migrate
    
# Create super user:
    python manage.py createsuperuser
    
# Run server:
    python manage.py runserver
    

Urls
-----------------
'api/posts/' - all posts <br />
'api/post/<pk>' - post by pk <br />
'api/post/<pk>/like' - like post  <br />
'api/post/analytics' - analytic posts by days <br />
'account/register/' - register new account <br />
'account/all/' - all accounts <br />
'account/login/' - login to account

   