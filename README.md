"#Alx_CapstoneProject" 
# Expense Tracker API

## OverView
This project is a backend API for an expense tracking system. User can:
-Register, login, logout
-Create, Update, and delete expenses
-Organizes expenses into categories
-view their personal expenses securely

Built Using Django, Django REST Framework, and PostgreSQL


## Features 
-User authentication (register, login, logout)
-CRUD operations for expenses 
-CRUD operations for categories
-secure user-specific data access

## Installation
clone the repository 
git clone https://github.com/abdelrahmanm0hammed/Alx_CapstoneProject

cd Expense_tracker

python -m venv venv 
venv\scripts\activate

python manage.py migrate 

python manage.py createsuperuser

python manage.py runserver

## Technolog Stack 
-Python 3.14
-Django 5.2.7
-Django REST Framework
-PostgreSQL

## Usage

### Register a user 
Visit the registeration page
http://127.0.0.1:8000/accounts/register/
fill in th HTML form with :
First Name 
Last Name 
Username
Email
Password
Confirm Password

Click Submit

Behavior: 
Redirects to login page on success:
show a message if :
    Username is taken
    Email is taken
    Password dont match

## Login
Visit the login page 
http://127.0.0.1:8000/accounts/login/

Fill in the HTML form with :
Username 
Password 

Click submit 

Behavior:
Redirects to home page on successful login
Show a message if credentials are invalid


## Logout

Visit the logout page
http://127.0.0.1:8000/accounts/logout/

Behavior:
Logs the user out
Redirects to home page

## Usage Example 

register user
http://127.0.0.1:8000/accounts/register/
Firstname : john
Secondname : Doe
Username : abood    
Password : 123456abdo
Confirm Password : 123456abdo
Email : myemail@gmail.com

another user 

Firstname : john
Secondname : micheal
Username : abood1   
Password : 123456abdo
Confirm Password : 123456abdo
Email : myemail1@gmail.com

login the first user 
visit the page 
http://127.0.0.1:8000/accounts/login/
username :abood
password : 123456abdo


create a category:
visit the page
http://127.0.0.1:8000/categories/
name : Electronics
Description : Devices that work using electricity or batteries
user -> automatically assigned to the logged in user 
created at -> automatically assigned to the current date and time

create an expense:
visit the page 
http://127.0.0.1:8000/expenses/
Category : choose a category from the past created categories i.e Electronics
Amount : 100 $
Description : a Mobile phone 
Date : Enter the date i.e Today

logout 
visit the page 
http://127.0.0.1:8000/accounts/logout/

## Another example 

login the second user 
visit the page 
http://127.0.0.1:8000/accounts/login/
username :abood1
password : 123456abdo


create a category:
visit the page
http://127.0.0.1:8000/categories/
name : Vegatables 
Description : Healthy food
user -> automatically assigned to the logged in user 
created at -> automatically assigned to the current date and time

create an expense:
visit the page 
http://127.0.0.1:8000/expenses/
Category : choose a category from the past created categories i.e Vegetables
Amount : 10 $
Description : one kilo tomato and one kilo potato
Date : Enter the date i.e Today

logout 
visit the page 
http://127.0.0.1:8000/accounts/logout/

