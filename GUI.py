import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to SQLite database
def connect_database():
    connection = sqlite3.connect("university_management_system.db")
    cursor = connection.cursor()
    cursor.executescript("""
    PRAGMA foreign_keys = ON;
    """)
    return connection, cursor

# Function to view all students
def view_students():
    connection, cursor = connect_database()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    connection.close()

    # Clear the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert data into the treeview
    for row in rows:
        tree.insert("", "end", values=row)

# Function to add a new student
def add_student():
    name = student_name_entry.get()
    dob = student_dob_entry.get()
    gender = student_gender_var.get()
    phone = student_phone_entry.get()

    if not name or not dob or not gender or not phone:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    connection, cursor = connect_database()
    cursor.execute("INSERT INTO Students (StudentName, DateOfBirth, Gender, PhoneNumber) VALUES (?, ?, ?, ?)", 
                   (name, dob, gender, phone))
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Student added successfully!")
    view_students()

# Function to enroll a student 
def enroll_student():
    student_id = enroll_student_id_entry.get()
    course_id = enroll_course_id_entry.get()

    if not student_id or not course_id:
        messagebox.showerror("Input Error", "Both Student ID and Course ID are required!")
        return

    connection, cursor = connect_database()
    try:
        cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", (student_id, course_id))
        connection.commit()
        messagebox.showinfo("Success", "Student enrolled successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Invalid Student ID or Course ID!")
    finally:
        connection.close()

# The main GUI window
root = tk.Tk()
root.title("University Management System")
root.geometry("800x600")

# Tabs for different functionality
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# View Students
view_students_tab = ttk.Frame(notebook)
notebook.add(view_students_tab, text="View Students")

# Display students
tree = ttk.Treeview(view_students_tab, columns=("ID", "Name", "DOB", "Gender", "Phone"), show="headings")
tree.pack(expand=True, fill="both", padx=10, pady=10)

tree.heading("ID", text="Student ID")
tree.heading("Name", text="Name")
tree.heading("DOB", text="Date of Birth")
tree.heading("Gender", text="Gender")
tree.heading("Phone", text="Phone Number")

# Refresh student list
refresh_button = ttk.Button(view_students_tab, text="Refresh", command=view_students)
refresh_button.pack(pady=10)

# Add Students
add_students_tab = ttk.Frame(notebook)
notebook.add(add_students_tab, text="Add Student")

# Input for adding a student
ttk.Label(add_students_tab, text="Student Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
student_name_entry = ttk.Entry(add_students_tab)
student_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ttk.Label(add_students_tab, text="Date of Birth (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
student_dob_entry = ttk.Entry(add_students_tab)
student_dob_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

ttk.Label(add_students_tab, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
student_gender_var = tk.StringVar(value="Male")
ttk.Combobox(add_students_tab, textvariable=student_gender_var, values=["Male", "Female"]).grid(row=2, column=1, padx=10, pady=5, sticky="w")

ttk.Label(add_students_tab, text="Phone Number:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
student_phone_entry = ttk.Entry(add_students_tab)
student_phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Add a student
add_student_button = ttk.Button(add_students_tab, text="Add Student", command=add_student)
add_student_button.grid(row=4, column=0, columnspan=2, pady=10)

# Enroll Students
enroll_students_tab = ttk.Frame(notebook)
notebook.add(enroll_students_tab, text="Enroll Student")

ttk.Label(enroll_students_tab, text="Student ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
enroll_student_id_entry = ttk.Entry(enroll_students_tab)
enroll_student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ttk.Label(enroll_students_tab, text="Course ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
enroll_course_id_entry = ttk.Entry(enroll_students_tab)
enroll_course_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Enroll a student
enroll_student_button = ttk.Button(enroll_students_tab, text="Enroll Student", command=enroll_student)
enroll_student_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run GUI
view_students()
root.mainloop()
