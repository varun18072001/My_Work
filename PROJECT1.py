from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import mysql.connector

# Create a connection to MySQL database
mydb = mysql.connector.connect(host="localhost", user="root", port="3306", password = "@Vks1871", database = "employee_database")

# Create a cursor object to interact with the database
mycursor = mydb.cursor()
dbs = mycursor.execute('CREATE TABLE emp(emp_no integer(10) PRIMARY KEY,name VARCHAR(25),email VARCHAR(25),phone_number integer(10),place VARCHAR(25)')

# Function to save employee details to MySQL database
def save_employee_details(emp_no, emp_details):
    sql = "INSERT INTO emp (emp_no, name, email, phone_number, place) VALUES (%s, %s, %s, %s, %s)"
    values = (emp_no, emp_details['name'], emp_details['email'], emp_details['phone number'], emp_details['place'])
    mycursor.execute(sql, values)
    mydb.commit()


# Function to load employee details from MySQL database
def load_employee_details():
    mycursor.execute("SELECT * FROM employees")
    rows = mycursor.fetchall()
    for row in rows:
        emp_no = row[0]
        emp_details = {'name': row[1], 'email': row[2], 'phone number': row[3], 'place': row[4]}
        emp_database[emp_no] = emp_details


# File to store employee details
FILE_NAME = "employee_details.txt"


# fun() to add new employee
def add_employee():
    emp_no = int(emp_no_entry.get())
    name = name_entry.get()
    email = email_entry.get()
    phone = int(ph_no_entry.get())
    place = place_entry.get()

    # create a dictionary for employee
    emp_details = {'name': name, 'email': email, 'phone number': phone, 'place': place}
    emp_database[emp_no] = emp_details

    # clear the fields
    emp_no_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    ph_no_entry.delete(0, END)
    place_entry.delete(0, END)

    # Save employee details to MySQL database after adding
    save_employee_details(emp_no, emp_details)

    # Create a message displaying the added employee details
    message = f"Employee Number: {emp_no}\nName: {name}\nEmail: {email}\nPhone Number: {phone}\nPlace: {place}"
    messagebox.showinfo("Employee Added", message)


# Load employee details when the application starts
emp_database = {}
load_employee_details()


# fun() to delete employee details
def del_employee():
    emp_no = int(emp_no_entry_del.get())  # Retrieve the employee number for deletion
    if emp_no in emp_database:
        del_details = del_details_entry.get()
        if del_details in emp_database[emp_no]:
            deleted_value = emp_database[emp_no][del_details]  # Store the deleted value for reference
            del emp_database[emp_no][del_details]
            messagebox.showinfo('Success', f'{del_details} deleted for employee {emp_no}')

            # Display the updated details in a messagebox
            updated_details = f'Updated Details for Employee {emp_no}:\n\n'
            for key, value in emp_database[emp_no].items():
                updated_details += f'{key}: {value}\n'
            messagebox.showinfo('Updated Details', updated_details)

            # Display the deleted detail
            messagebox.showinfo('Deleted Detail', f'{del_details}: {deleted_value} is deleted.')
        else:
            messagebox.showinfo('Error', 'Invalid detail provided or detail not found.')
    else:
        messagebox.showinfo('Error', 'Employee not found in the database.')


# fun() to Edit employee details
def edit_employee():
    emp_no = int(emp_no_entry_edit.get())  # Retrieve the employee number for editing
    if emp_no in emp_database:
        edit_details = edit_details_entry.get()
        if edit_details in emp_database[emp_no]:
            new_emp_detail = input("Enter new detail: ")  # Get the new detail from user
            emp_database[emp_no][edit_details] = new_emp_detail
            messagebox.showinfo('Success', f'{edit_details} updated for employee {emp_no}')

            # Display the updated details in a messagebox
            updated_details = f'Updated Details for Employee {emp_no}:\n\n'
            for key, value in emp_database[emp_no].items():
                updated_details += f'{key}: {value}\n'
            messagebox.showinfo('Updated Details', updated_details)
        else:
            messagebox.showinfo('Error', 'Invalid detail provided or detail not found.')
    else:
        messagebox.showinfo('Error', 'Employee not found in the database.')


# fun() to Get employee details
def get_employee():
    emp_no = int(emp_no_entry_get.get())  # Retrieve the employee number to get details
    if emp_no in emp_database:
        get_details = get_details_entry.get()
        if get_details in emp_database[emp_no]:
            messagebox.showinfo(f'{get_details} for employee {emp_no}:', emp_database[emp_no][get_details])
        else:
            messagebox.showinfo('Error', 'Invalid detail provided or detail not found.')
    else:
        messagebox.showinfo('Error', 'Employee not found in the database.')


# fun() to close
def close_window():
    if messagebox.askokcancel("Close", "Do you want to close the application?"):
        window.destroy()


# Create main window
window = Tk()
window.title('Employee Database')

# Create a Notebook (tab manager)
notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Add Tab
add_tab = ttk.Frame(notebook)
notebook.add(add_tab, text='Add Employee')

# Adding New Employee

# Employee Number
ttk.Label(add_tab, text='Employee Number:').grid(column=0, row=0, sticky=W, padx=5, pady=5)
emp_no_entry = ttk.Entry(add_tab)
emp_no_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# Name
ttk.Label(add_tab, text='Name:').grid(column=0, row=1, sticky=W, padx=5, pady=5)
name_entry = ttk.Entry(add_tab)
name_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# Phone Number
ttk.Label(add_tab, text='Phone Number:').grid(column=0, sticky=W, row=2, padx=5, pady=5)
ph_no_entry = ttk.Entry(add_tab)
ph_no_entry.grid(column=1, row=2, sticky=E, padx=5, pady=5)

# Email ID
ttk.Label(add_tab, text='Email ID:').grid(column=0, row=3, sticky=W, padx=5, pady=5)
email_entry = ttk.Entry(add_tab)
email_entry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

# Place
ttk.Label(add_tab, text='Place:').grid(column=0, row=4, sticky=W, padx=5, pady=5)
place_entry = ttk.Entry(add_tab)
place_entry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

# Submit
add_button = ttk.Button(add_tab, text="Add", command=add_employee)
add_button.grid(column=1, row=5, sticky=S, padx=5, pady=5)

# Delete Tab
del_tab = ttk.Frame(notebook)
notebook.add(del_tab, text='Delete Employee')

# Employee Number to Delete
ttk.Label(del_tab, text='Employee Number to Delete:').grid(column=0, row=0, sticky=W, padx=5, pady=5)
emp_no_entry_del = ttk.Entry(del_tab)
emp_no_entry_del.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# Detail to Delete
ttk.Label(del_tab, text='Detail to Delete:').grid(column=0, row=1, sticky=W, padx=5, pady=5)
del_details_entry = ttk.Entry(del_tab)
del_details_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# Delete button
del_button = ttk.Button(del_tab, text='Delete', command=del_employee)
del_button.grid(column=1, row=2, sticky=E, padx=5, pady=5)

# Edit
edit_tab = ttk.Frame(notebook)
notebook.add(edit_tab, text='Edit Employee')

# Employee Number to Edit
ttk.Label(edit_tab, text='Employee Number to Edit:').grid(column=0, row=0, sticky=W, padx=5, pady=5)
emp_no_entry_edit = ttk.Entry(edit_tab)
emp_no_entry_edit.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# Employee Details to edit
ttk.Label(edit_tab, text='Detail to Edit:').grid(column=0, row=1, sticky=W, padx=5, pady=5)
edit_details_entry = ttk.Entry(edit_tab)
edit_details_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# Edit button
edit_button = ttk.Button(edit_tab, text='Edit', command=edit_employee)
edit_button.grid(column=1, row=2, sticky=E, padx=5, pady=5)

# Get
get_tab = ttk.Frame(notebook)
notebook.add(get_tab, text='Get Employee')

# Employee Number to Get
ttk.Label(get_tab, text='Employee Number to Get:').grid(column=0, row=0, sticky=W, padx=5, pady=5)
emp_no_entry_get = ttk.Entry(get_tab)
emp_no_entry_get.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# Employee Details to Get
ttk.Label(get_tab, text='Detail to Get:').grid(column=0, row=1, sticky=W, padx=5, pady=5)
get_details_entry = ttk.Entry(get_tab)
get_details_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# Get button
get_button = ttk.Button(get_tab, text='Get', command=get_employee)
get_button.grid(column=1, row=2, sticky=E, padx=5, pady=5)

# Close button
close_button = ttk.Button(window, text='Close', command=close_window)
close_button.pack(pady=10)

window.mainloop()