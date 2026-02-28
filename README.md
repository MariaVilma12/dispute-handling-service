# Dispute Handling Service (Console-Based)

## Overview

The Dispute handling service is a console-based backend application developed using Python and MySQL.  
It is designed to manage the full lifecycle of disputes, including creation, assignment, tracking, and resolution, with secure authentication and role-based access control.
The project simulates a real-world enterprise system used in domains such as construction projects, corporate operations, or service management.


## Features

### Core Functionality
- User management with roles
- Dispute creation and tracking
- Assignment of disputes to responsible users
- Status updates throughout the dispute lifecycle
- Console-based user interface

### Authentication & Security
- Secure login system
- Password hashing using SHA-256
- Role-based access control:
  - **Admin** – Full system access
  - **Manager** – Manage and resolve disputes
  - **Viewer** – Read-only access

    
## User Roles & Permissions
```
   Role      Permissions 
|---------|-------------------------------------------------|
| Admin   | Register users, manage disputes, view all data  |
| Manager | Create, assign and update disputes              |
| Viewer  | View disputes only                              |
```

## Technology Stack
- Python 
- MySQL
- PyCharm IDE
- Console Interface


## Project Structure
```
Python_DMS
│
├── dat.py # Database connection
├── auth.py # Authentication & password hashing
├── user.py # User operations
├── dispute.py # Dispute operations
├── main.py # Console UI & application flow
└── README.md
```

Username: admin
Password: admin123