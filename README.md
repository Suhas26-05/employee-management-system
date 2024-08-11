
# Employee Management System

## Overview

The Employee Management System is a desktop application built with Python's Tkinter library and SQLite. This application allows users to manage employee records with functionalities to add, remove, promote, and view employee details.

## Features

- **Add Employee**: Input and store employee details such as ID, name, age, department, position, and salary.
- **Remove Employee**: Remove an employee record based on their ID.
- **Promote Employee**: Update the salary of an employee.
- **Display Employees**: View all employee records in a table format.

## Installation

To run the Employee Management System, you'll need Python installed on your machine. This project has been tested with Python 3.x.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Suhas26-05/employee-management-system.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd employee-management-system
   ```

3. **Install any required libraries:**

   This project requires the `sqlite3` and `tkinter` libraries, which are included with Python's standard library. No additional installation is required for these libraries.

## Usage

1. **Run the application:**

   Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

2. **Interact with the Application:**

   - **Toggle Theme:** Switch between light and dark themes using the "Theme" button.
   - **Add Employee:** Click the "Add Employee" button to open a dialog where you can enter employee details.
   - **Remove Employee:** Click the "Remove Employee" button and provide the employee ID to remove an employee record.
   - **Promote Employee:** Click the "Promote Employee" button to update an employee's salary.
   - **Display Employees:** Click the "All Employees Details" button to view all employee records in a new window.

## Database

The application uses SQLite to store employee records. The database file (`employee.db`) will be created in the same directory as the script if it does not already exist. The database contains a single table:

- **employees**:
  - `Id` (INTEGER PRIMARY KEY): Unique identifier for each employee.
  - `name` (TEXT): Name of the employee.
  - `age` (INTEGER): Age of the employee.
  - `dept` (TEXT): Department where the employee works.
  - `pos` (TEXT): Position of the employee.
  - `salary` (REAL): Salary of the employee.

## Contributing

Contributions to this project are welcome. If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- This project uses [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface and [SQLite](https://www.sqlite.org/index.html) for the database.


### Instructions for the README:

1. **Overview:** Provides a brief introduction to what the application does.
2. **Features:** Lists the main functionalities of the application.
3. **Installation:** Details the steps to clone the repository and install any required libraries.
4. **Usage:** Instructions on how to run the application and interact with it.
5. **Database:** Explains the database schema and how the application stores data.
6. **Contributing:** Guidelines for contributing to the project.
7. **License:** Information about the license under which the project is distributed.
8. **Acknowledgements:** Credits and links to resources used in the project.
9. **Contact:** Provides a way for users to reach out for questions or feedback.

Feel free to adjust the content to better fit your project's specifics and your preferences.
