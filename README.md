# Expense Tracker API

A backend API for managing personal expenses and financial records.

Overview

The Expense Tracker API allows users to securely track their expenses, organize them into categories, and generate financial reports.

The system supports:

Session-based authentication for web users

JWT authentication for API clients

This project was developed as part of a Capstone Project using modern backend technologies.

Features
- Authentication

User registration

User login and logout

JWT authentication

Token refresh

Token blacklisting (secure logout)

Expense Management

Create expenses

Update expenses

Delete expenses

View personal expenses

Categories

Create categories

Update categories

Delete categories

Assign expenses to categories

Reports

Monthly expense reports

Yearly grouped reports

API Features

Filtering

Pagination

Secure user-specific data access

CSV export

Interactive API documentation

## Technology Stack

Technology	Purpose
Python 3.14	Programming language
Django	Web framework
Django REST Framework	API framework
PostgreSQL	Database
SimpleJWT	JWT authentication
drf-spectacular	API documentation

## Installation

1 Clone the Repository
git clone https://github.com/abdelrahmanm0hammed/Alx_CapstoneProject
2 Navigate to the Project Folder
cd Expense_tracker
3 Create Virtual Environment
python -m venv venv
4 Activate Virtual Environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
5 Install Dependencies
pip install -r requirements.txt
6 Run Database Migrations
python manage.py migrate
7 Create Admin User
python manage.py createsuperuser
8 Start Development Server
python manage.py runserver

Server will start at:

http://127.0.0.1:8000
API Documentation

Interactive Swagger documentation:

http://127.0.0.1:8000/api/docs/

OpenAPI schema:

http://127.0.0.1:8000/api/schema/

This interface allows developers to:

Explore endpoints

Test requests

View request and response formats

Authentication

The API uses JWT authentication for secure access.

Obtain Access Token

Endpoint

POST /api/token/

Request

{
  "username": "your_username",
  "password": "your_password"
}

Response

{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}

Use the access token in authenticated requests:

Authorization: Bearer ACCESS_TOKEN
Refresh Access Token
POST /api/token/refresh/

Request:

{
  "refresh": "REFRESH_TOKEN"
}
Logout (Blacklist Refresh Token)
POST /api/logout/

Request:

{
  "refresh": "REFRESH_TOKEN"
}
API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/token/	Obtain JWT tokens
POST	/api/token/refresh/	Refresh access token
POST	/api/logout/	Logout and blacklist refresh token
User Registration (HTML Form)

Users can register via the registration page:

/accounts/register/
Required Fields

First Name

Last Name

Username

Email

Password

Confirm Password

Behavior

Successful registration:

Redirects user to login page

Error handling:

Username already exists

Email already exists

Passwords do not match

Login
/accounts/login/
Input

Username

Password

Behavior

Successful login:

Redirects user to home page

Invalid credentials:

Displays error message

Logout
/accounts/logout/
Behavior

Logs the user out

Redirects to the home page

Categories API
Create Category
POST /categories/

Example request:

{
  "name": "Electronics",
  "description": "Devices that work using electricity"
}
Behavior

Logged-in user is automatically assigned

Creation date is automatically recorded

Expenses API
Create Expense
POST /expenses/

Example request:

{
  "category": 1,
  "amount": 100,
  "description": "Mobile phone",
  "date": "2026-03-07"
}
Retrieve Expenses
GET /expenses/

Supported features:

Filtering

Pagination

Ordering

Example query:

/expenses/?category=1
Reports
Monthly Report
GET /reports/monthly/?year=2026&month=3

Returns the total expenses for a specific month.

Yearly Report
GET /reports/yearly/?year=2026

Returns expense totals grouped by month.

Example Usage (Step-by-Step)
Step 1 — Register a User

Visit:

http://127.0.0.1:8000/accounts/register/

Example input:

First Name: John
Last Name: Doe
Username: abood
Email: myemail@gmail.com
Password: 123456abdo

After submission:

User is redirected to login page.

Step 2 — Login

Visit:

http://127.0.0.1:8000/accounts/login/

Credentials:

Username: abood
Password: 123456abdo

User will be redirected to the home page.

Step 3 — Create a Category

Visit:

http://127.0.0.1:8000/categories/

Example:

Name: Electronics
Description: Devices powered by electricity

User is automatically assigned.

Step 4 — Create an Expense

Visit:

http://127.0.0.1:8000/expenses/

Example:

Category: Electronics
Amount: 100
Description: Mobile phone
Date: Today
Step 5 — Logout

Visit:

http://127.0.0.1:8000/accounts/logout/

User is logged out and redirected to home page.

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

The application ensures:

User-specific data isolation

Secure JWT authentication

Refresh token invalidation on logout

License

This project was created as part of a Capstone Project.
