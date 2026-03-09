# Expense Tracker API
# Expense Tracker API

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![DRF](https://img.shields.io/badge/Django%20REST-API-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

A backend API for managing personal expenses and financial records.

---

# Overview

The **Expense Tracker API** allows users to securely track their expenses, organize them into categories, and generate financial reports.

The system supports:

- **Session-based authentication** for web users
- **JWT authentication** for API clients

This project was developed as part of a **Capstone Project** using modern backend technologies.

---
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Reports](#reports)
- [Example Usage](#example-usage-step-by-step)
- [Project Structure](#project-structure)
- [Security](#security)
- [License](#license)

# Features

## 1. Authentication

- User registration
- User login and logout
- JWT authentication
- Token refresh
- Token blacklisting (secure logout)

---

## 2. Expense Management

- Create expenses
- Update expenses
- Delete expenses
- View personal expenses

---

## 3. Categories

- Create categories
- Update categories
- Delete categories
- Assign expenses to categories

---

## 4. Reports

- Monthly expense reports
- Yearly grouped reports

---

## 5. API Features

- Filtering
- Pagination
- Secure user-specific data access
- CSV export
- Interactive API documentation

---

# Technology Stack

| Technology | Purpose |
|-----------|--------|
| Python 3.14 | Programming language |
| Django | Web framework |
| Django REST Framework | API framework |
| PostgreSQL | Database |
| SimpleJWT | JWT authentication |
| drf-spectacular | API documentation |

---
# System Architecture

```mermaid
graph TD

User --> Browser
Browser --> DjangoApp
DjangoApp --> DRF_API
DRF_API --> PostgreSQL

DjangoApp --> Authentication
Authentication --> JWT
JWT --> ProtectedEndpoints

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/abdelrahmanm0hammed/Alx_CapstoneProject
## 2. Navigate to the Project Folder

```bash
cd Expense_tracker
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Database Migrations

```bash
python manage.py migrate
```

---

## 7. Create Admin User

```bash
python manage.py createsuperuser
```

---

## 8. Start Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

### Interactive Swagger Documentation

```
http://127.0.0.1:8000/api/docs/
```

### OpenAPI Schema

```
http://127.0.0.1:8000/api/schema/
```

The documentation interface allows developers to:

* Explore endpoints
* Test API requests
* View request and response formats

---

# Authentication

The API uses **JWT authentication** for secure access.

---

## Obtain Access Token

### Endpoint

```
POST /api/token/
```

### Request

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Response

```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

Use the access token in authenticated requests:

```
Authorization: Bearer ACCESS_TOKEN
```

---

## Refresh Access Token

### Endpoint

```
POST /api/token/refresh/
```

### Request

```json
{
  "refresh": "REFRESH_TOKEN"
}
```

---

## Logout (Blacklist Refresh Token)

### Endpoint

```
POST /api/logout/
```

### Request

```json
{
  "refresh": "REFRESH_TOKEN"
}
```

---

# API Endpoints

## Authentication Endpoints

| Method | Endpoint            | Description                        |
| ------ | ------------------- | ---------------------------------- |
| POST   | /api/token/         | Obtain JWT tokens                  |
| POST   | /api/token/refresh/ | Refresh access token               |
| POST   | /api/logout/        | Logout and blacklist refresh token |

---

# User Registration (HTML Form)

Users can register using the registration page:

```
/accounts/register/
```

### Required Fields

* First Name
* Last Name
* Username
* Email
* Password
* Confirm Password

### Behavior

**Successful Registration**

* User is redirected to the login page.

**Error Handling**

* Username already exists
* Email already exists
* Passwords do not match

---

# Login

### Endpoint

```
/accounts/login/
```

### Input

* Username
* Password

### Behavior

**Successful Login**

* User is redirected to the home page.

**Invalid Credentials**

* Displays an error message.

---

# Logout

### Endpoint

```
/accounts/logout/
```

### Behavior

* Logs the user out
* Redirects to the home page

---

# Categories API

## Create Category

### Endpoint

```
POST /categories/
```

### Example Request

```json
{
  "name": "Electronics",
  "description": "Devices that work using electricity"
}
```

### Behavior

* Logged-in user is automatically assigned
* Creation date is automatically recorded

---

# Expenses API

## Create Expense

### Endpoint

```
POST /expenses/
```

### Example Request

```json
{
  "category": 1,
  "amount": 100,
  "description": "Mobile phone",
  "date": "2026-03-07"
}
```

---

## Retrieve Expenses

### Endpoint

```
GET /expenses/
```

### Supported Features

* Filtering
* Pagination
* Ordering

### Example Query

```
/expenses/?category=1
```

---

# Reports

## Monthly Report

### Endpoint

```
GET /reports/monthly/?year=2026&month=3
```

Returns the **total expenses for a specific month**.

---

## Yearly Report

### Endpoint

```
GET /reports/yearly/?year=2026
```

Returns **expense totals grouped by month**.

---

# Example Usage (Step-by-Step)

## Step 1 — Register a User

Visit:

```
http://127.0.0.1:8000/accounts/register/
```

Example Input:

* First Name: John
* Last Name: Doe
* Username: abood
* Email: [myemail@gmail.com](mailto:myemail@gmail.com)
* Password: 123456abdo

After submission:

* User is redirected to the login page.

---

## Step 2 — Login

Visit:

```
http://127.0.0.1:8000/accounts/login/
```

Credentials:

* Username: abood
* Password: 123456abdo

Result:

* User is redirected to the home page.

---

## Step 3 — Create a Category

Visit:

```
http://127.0.0.1:8000/categories/
```

Example:

* Name: Electronics
* Description: Devices powered by electricity

The user is automatically assigned.

---

## Step 4 — Create an Expense

Visit:

```
http://127.0.0.1:8000/expenses/
```

Example:

* Category: Electronics
* Amount: 100
* Description: Mobile phone
* Date: Today

---

## Step 5 — Logout

Visit:

```
http://127.0.0.1:8000/accounts/logout/
```

Result:

* User is logged out
* Redirected to the home page

---

# Project Structure

```
Expense_Tracker
│
├── users
├── expenses
├── categories
├── reports
├── manage.py
├── requirements.txt
└── README.md
```

---

# Security

The application ensures:

* User-specific data isolation
* Secure JWT authentication
* Refresh token invalidation on logout

---

# License

This project was created as part of a **Capstone Project**.

