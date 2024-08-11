import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("700x700")
        self.is_on = True
        root.configure(bg="Black")

        # Initialize the user interface
        self.create_ui()

    def create_ui(self):
        # Toggle theme button
        self.toggle_button = tk.Button(self.root, text="Theme", command=self.switch,
               activebackground="Grey", 
               activeforeground="White",
               bg="White",
               fg="Black",
               cursor="hand2")
        self.toggle_button.pack(pady=10, anchor="e")

        # Create the employee table in the database
        self.create_table()

        # Status label
        self.status_label = tk.Label(self.root, text="Welcome to Employee Management Record")
        self.status_label.pack(pady=10)
        self.status_label.config(bg="black", fg="White")

        # Buttons for various operations
        self.Add_button = tk.Button(self.root, 
                   text="Add Employee", 
                   command=self.show_add_employee_dialog,
                   activebackground="Sky Blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="white",
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 7),
                   height=1,
                   highlightbackground="White",
                   highlightcolor="green",
                   highlightthickness=2,
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
        self.Add_button.pack(pady=10)

        self.Remove_button = tk.Button(self.root, 
                   text="Remove Employee", command=self.Remove_employee,
                   activebackground="Red", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="white",
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 7),
                   height=1,
                   highlightbackground="White",
                   highlightcolor="green",
                   highlightthickness=2,
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
        self.Remove_button.pack(pady=10)

        self.Promote_button = tk.Button(self.root, text="Promote Employee", command=self.Promote_employee,
                   activebackground="Green", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="White",
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 7),
                   height=1,
                   highlightbackground="White",
                   highlightcolor="green",
                   highlightthickness=2,
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
        self.Promote_button.pack(pady=10)

        self.Display_button = tk.Button(self.root, text="All Employees Details", command=self.Display_employees,
                   activebackground="Black", 
                   activeforeground="white",
                   anchor="center",
                   bd=2,
                   bg="white",
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 7),
                   height=1,
                   highlightbackground="White",
                   highlightcolor="green",
                   highlightthickness=2,
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
        self.Display_button.pack(pady=10)

    def switch(self):
        # Toggle between dark and light themes
        self.is_on = not self.is_on
        if self.is_on:
            self.root.config(bg="Black")
            self.status_label.config(bg="black", fg="White")
        else:
            self.root.config(bg="White")
            self.status_label.config(bg="White", fg="Black")

    def create_table(self):
        # Connect to SQLite database and create the employees table if it doesn't exist
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS employees (
                            Id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            dept TEXT NOT NULL,
                            pos TEXT NOT NULL,
                            salary REAL NOT NULL
                        )''')

        conn.commit()
        conn.close()

    def show_add_employee_dialog(self):
        # Create a dialog window to input employee details
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Employee")

        tk.Label(dialog, text="Id").grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(dialog)
        id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Name").grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(dialog)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Age").grid(row=2, column=0, padx=10, pady=5)
        age_entry = tk.Entry(dialog)
        age_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Department").grid(row=3, column=0, padx=10, pady=5)
        dept_entry = tk.Entry(dialog)
        dept_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Position").grid(row=4, column=0, padx=10, pady=5)
        pos_entry = tk.Entry(dialog)
        pos_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Salary").grid(row=5, column=0, padx=10, pady=5)
        salary_entry = tk.Entry(dialog)
        salary_entry.grid(row=5, column=1, padx=10, pady=5)

        def add_employee():
            # Add the employee to the database
            Id = id_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            dept = dept_entry.get()
            pos = pos_entry.get()
            salary = salary_entry.get()

            if Id and name and age and dept and pos and salary:
                conn = sqlite3.connect('employee.db')
                c = conn.cursor()
                try:
                    c.execute("INSERT INTO employees (Id, name, age, dept, pos, salary) VALUES (?, ?, ?, ?, ?, ?)",
                              (Id, name, age, dept, pos, salary))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee added successfully!")
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Employee ID already exists")
                finally:
                    conn.close()
            else:
                messagebox.showerror("Error", "All fields are required")

            dialog.destroy()

        tk.Button(dialog, text="Add Employee", command=add_employee).grid(row=6, column=0, columnspan=2, pady=10)

    def Remove_employee(self):
        # Prompt for employee ID and remove the employee from the database
        emp_id = simpledialog.askstring("Remove Employee", "Enter Employee ID:")
        if emp_id:
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("DELETE FROM employees WHERE Id=?", (emp_id,))
            if c.rowcount == 0:
                messagebox.showerror("Error", "Employee ID not found")
            else:
                conn.commit()
                messagebox.showinfo("Success", "Employee removed successfully!")
            conn.close()
        else:
            messagebox.showerror("Error", "Employee ID is required")

    def Promote_employee(self):
        # Prompt for employee ID and new salary, then update the salary in the database
        emp_id = simpledialog.askstring("Promote Employee", "Enter Employee ID:")
        emp_sal = simpledialog.askstring("Promote Employee", "Enter New Salary:")

        if emp_id and emp_sal:
            conn = sqlite3.connect('employee.db')
            c = conn.cursor()
            c.execute("UPDATE employees SET salary = ? WHERE Id = ?", (emp_sal, emp_id))
            if c.rowcount == 0:
                messagebox.showerror("Error", "Employee ID not found")
            else:
                conn.commit()
                messagebox.showinfo("Success", "Employee promoted successfully!")
            conn.close()
        else:
            messagebox.showerror("Error", "Employee ID and new salary are required")

    def Display_employees(self):
        # Retrieve and display all employee details in a new window
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employees")
        rows = c.fetchall()
        conn.close()

        # Create a new window to display employee details
        display_window = tk.Toplevel(self.root)
        display_window.title("Employee Details")

        # Create a table to display employee data
        tree = ttk.Treeview(display_window, columns=("Id", "Name", "Age", "Department", "Position", "Salary"), show='headings')
        tree.heading("Id", text="Id")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Department", text="Department")
        tree.heading("Position", text="Position")
        tree.heading("Salary", text="Salary")

        # Insert employee data into the table
        for row in rows:
            tree.insert("", tk.END, values=row)
        
        tree.pack(expand=True, fill=tk.BOTH)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
