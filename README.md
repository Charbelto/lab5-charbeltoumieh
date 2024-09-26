
# User Management API

This project provides a basic RESTful API to manage user information using Flask and SQLite. It allows operations such as creating, reading, updating, and deleting users in the database.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Features

- **SQLite Database** for storing user details (name, email, phone, address, country).
- Basic **CRUD operations**:
  - Create a new user
  - Read user data (fetch all users or specific user by ID)
  - Update existing user data
  - Delete a user
- **Flask** used as the web framework.
- **Flask-CORS** for enabling cross-origin requests.

## Requirements

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- SQLite3

You also need to install the required Python packages:

```bash
pip install -r requirements.txt
```

Where `requirements.txt` should contain:
```
Flask
Flask-CORS
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Charbelto/lab5-charbeltoumieh
   cd lab5-charbeltoumieh
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python Database.py
   ```

4. The API will now be available at `http://127.0.0.1:5000`.

## Usage

- The application starts by creating a SQLite database (`database.db`) and a `users` table if it doesn't exist.
- By default, a user named "Charbel Toumieh" is inserted into the table.

## API Endpoints

### Get all users
- **Endpoint**: `/api/users`
- **Method**: `GET`
- **Description**: Retrieve a list of all users.

### Get user by ID
- **Endpoint**: `/api/users/<user_id>`
- **Method**: `GET`
- **Description**: Retrieve a single user by their ID.

### Add a new user
- **Endpoint**: `/api/users/add`
- **Method**: `POST`
- **Description**: Add a new user to the database.
- **Body**:
  ```json
  {
    "name": "User Name",
    "email": "user@example.com",
    "phone": "123456789",
    "address": "User Address",
    "country": "User Country"
  }
  ```

### Update an existing user
- **Endpoint**: `/api/users/update`
- **Method**: `PUT`
- **Description**: Update an existing user's information.
- **Body**:
  ```json
  {
    "user_id": 1,
    "name": "Updated Name",
    "email": "updated@example.com",
    "phone": "987654321",
    "address": "Updated Address",
    "country": "Updated Country"
  }
  ```

### Patch a user's information
- **Endpoint**: `/api/users/patch/<user_id>`
- **Method**: `PATCH`
- **Description**: Partially update an existing user's information.
- **Body**:
  ```json
  {
    "email": "newemail@example.com"
  }
  ```

### Delete a user
- **Endpoint**: `/api/users/delete/<user_id>`
- **Method**: `DELETE`
- **Description**: Delete a user by their ID.

