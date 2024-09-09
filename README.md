# AI-Pair-Programming

# TaskManager

This project is an **experiment** where AI pair programming is utilized to build a simple task management application using **GitHub Copilot**. The majority of the code and features in this project were generated with assistance from GitHub Copilot, making it an interesting exploration of how AI can help in software development.

The TaskManager application is built with **Django** and **MongoDB**, using Djongo as the database backend. It allows users to add, delete, and mark tasks as complete. This project demonstrates how AI can assist in generating code, structuring projects, and solving common development challenges.

## Features

- Add new tasks with a description.
- Mark tasks as complete.
- Delete tasks.
- Simple, responsive frontend design.

## Requirements

To run this project, you'll need to have the following installed on your machine:

- **Python 3.9**
- **Django**
- **MongoDB**
- **Djongo** (MongoDB connector for Django)
- **Git**

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

   ```bash 
   git clone https://github.com/NisargPraj/AI-Pair-Programming.git 
   ```
2. **Navigate to the project directory**:

    ```bash
    cd TaskManager
    ```
3. **Install Virtual Environment**

    ```bash
    pip install virtualenv
    ```
4. **Create and Activate Virual Environment**

    ```bash
    # For Windows
    .venv\Scripts\activate  

    # For Mac/Linux
    source .venv/bin/activate  
    ```
5. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```
6. **Setup MongoDB**

    ```bash
    mongod
    ```
7. **Run Database Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. **Start the Server**
    ```bash
    python manage.py runserver
    ``` 

## License

This project is licensed under the [MIT License](./LICENSE).