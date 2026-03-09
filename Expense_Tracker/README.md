Expense Tracker API
Overview

Expense Tracker API is a backend system for managing personal finances.
It allows users to securely track expenses, organize them into categories, and generate financial reports.

The system supports both session-based authentication for web users and JWT authentication for API clients.

This project was built using Django, Django REST Framework, and PostgreSQL.

Features

User authentication (Register, Login, Logout)

JWT authentication for API access

CRUD operations for expenses

CRUD operations for categories

Secure user-specific data access

Monthly and yearly expense reports

Filtering and pagination

CSV export

Interactive API documentation (Swagger)

Technology Stack

Python 3.14

Django

Django REST Framework

PostgreSQL

SimpleJWT

drf-spectacular (API documentation)

Installation

Clone the repository

git clone https://github.com/abdelrahmanm0hammed/Alx_CapstoneProject

Navigate to the project folder

cd Expense_tracker

Create a virtual environment

python -m venv venv

Activate the virtual environment

Windows:

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run database migrations

python manage.py migrate

Create a superuser

python manage.py createsuperuser

Run the development server

python manage.py runserver

The project will be available at:

http://127.0.0.1:8000
API Documentation

Interactive API documentation is available at:

http://127.0.0.1:8000/api/docs/

OpenAPI schema:

http://127.0.0.1:8000/api/schema/
Authentication

The API supports JWT authentication.

Obtain JWT Tokens

Endpoint

POST /api/token/

Request body

{
  "username": "your_username",
  "password": "your_password"
}

Response

{
  "access": "access_token_here",
  "refresh": "refresh_token_here"
}

Use the access token in authenticated requests:

Authorization: Bearer ACCESS_TOKEN
API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/token/	Obtain JWT tokens
POST	/api/token/refresh/	Refresh access token
POST	/api/logout/	Logout and blacklist refresh token
User Registration (HTML Form)
GET /accounts/register/

Registers a new user.

Required fields:

First Name

Last Name

Username

Email

Password

Confirm Password

Behavior:

Redirects to login page after successful registration

Displays error messages if:

username already exists

email already exists

passwords do not match

Login
GET /accounts/login/

Login using username and password.

Behavior:

Redirects to home page on success

Displays an error message if credentials are invalid

Logout
GET /accounts/logout/

Logs the user out and redirects to the home page.

Categories API
Create Category
POST /categories/

Example request

{
  "name": "Electronics",
  "description": "Devices that work using electricity"
}

Behavior:

The logged-in user is automatically assigned as the category owner

Creation date is automatically recorded

Expenses API
Create Expense
POST /expenses/

Example request

{
  "category": 1,
  "amount": 100,
  "description": "Mobile phone",
  "date": "2026-03-07"
}
Retrieve Expenses
GET /expenses/

Supports:

filtering

pagination

ordering

Example:

/expenses/?category=1
Reports
Monthly Report
GET /reports/monthly/?year=2026&month=3

Returns total expenses for a specific month.

Yearly Report
GET /reports/yearly/?year=2026

Returns expense totals grouped by month.

Example Usage (Step-by-Step)
1 Register a User

Visit:

http://127.0.0.1:8000/accounts/register/

Example input:

First Name: John
Last Name: Doe
Username: abood
Email: myemail@gmail.com

Password: 123456abdo

Submit the form.

The user will be redirected to the login page.

2 Login

Visit:

http://127.0.0.1:8000/accounts/login/

Enter:

Username: abood
Password: 123456abdo

The user will be redirected to the home page.

3 Create a Category

Visit:

http://127.0.0.1:8000/categories/

Example:

Name: Electronics
Description: Devices powered by electricity

The logged-in user is automatically assigned.

4 Create an Expense

Visit:

http://127.0.0.1:8000/expenses/

Example:

Category: Electronics
Amount: 100
Description: Mobile phone
Date: Today

5 Logout

Visit:

http://127.0.0.1:8000/accounts/logout/

The user will be logged out and redirected to the home page.

Project Structure
Expense_Tracker
│
├── users
├── expenses
├── categories
├── reports
├── manage.py
├── requirements.txt
└── README.md
Security

User data is isolated per authenticated user

JWT tokens protect API endpoints

Refresh tokens can be blacklisted on logout

License

This project was developed as part of a Capstone Project