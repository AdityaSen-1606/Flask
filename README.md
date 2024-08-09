# Flask CRUD Application with MongoDB

## Overview

This is a simple CRUD (Create, Read, Update, Delete) application developed using Flask and MongoDB. It allows you to manage user records with functionality to add, edit, and delete users. Passwords are encrypted before being stored in the MongoDB database using `bcrypt`.

## Snapshots of Application

![AllUser](https://github.com/user-attachments/assets/32f9d9ee-3cfe-4bf5-b7af-1bad722cf7af?width=20&height=20)


## Features

- **Create Users**: Add new users with name, email, and password.
- **Read Users**: View a list of all users.
- **Update Users**: Edit user details with password verification.
- **Delete Users**: Remove users from the database.

## Installation

### Prerequisites

- Python 3.7 or higher
- MongoDB Atlas account
- [Git](https://git-scm.com/)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    
3. **Activate the Virtual Environment**

    On Windows
    ```bash
    git commit -m "Initial commit"

    On Linux
    ```bash
    source venv/bin/activate

4. **Install Dependencies**
   
   ```bash
   pip install -r requirements.txt

5. **Set Up Environment Variables**
 
    Create a .env file in the root directory and add your MongoDB connection URI:

    ```bash
    MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/dbname?retryWrites=true&w=majority"

6. **Run Application**

    ```bash
    flask run
