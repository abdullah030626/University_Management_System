import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
connection = sqlite3.connect("university_management_system.db")
cursor = connection.cursor()

# Step 1: Create Tables
cursor.executescript("""
-- Students Table
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentName TEXT NOT NULL,
    DateOfBirth DATE,
    Gender TEXT,
    PhoneNumber TEXT
);

-- Courses Table
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseName TEXT NOT NULL,
    Credits INTEGER NOT NULL,
    InstructorID INTEGER NOT NULL
);

-- Faculty Table
CREATE TABLE IF NOT EXISTS Faculty (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT NOT NULL,
    Department TEXT
);

-- Enrollments Table
CREATE TABLE IF NOT EXISTS Enrollments (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER NOT NULL,
    CourseID INTEGER NOT NULL,
    EnrollmentDate DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses (CourseID)
);

-- Grades Table
CREATE TABLE IF NOT EXISTS Grades (
    GradeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EnrollmentID INTEGER NOT NULL,
    Grade TEXT,
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments (EnrollmentID)
);
""")

# Step 2: Insert Sample Data
cursor.execute("INSERT INTO Faculty (FacultyName, Department) VALUES (?, ?)", ('Dr. John Smith', 'Computer Science'))
cursor.execute("INSERT INTO Faculty (FacultyName, Department) VALUES (?, ?)", ('Dr. Emily Brown', 'Mathematics'))

cursor.execute("INSERT INTO Courses (CourseName, Credits, InstructorID) VALUES (?, ?, ?)", ('Introduction to Programming', 3, 1))
cursor.execute("INSERT INTO Courses (CourseName, Credits, InstructorID) VALUES (?, ?, ?)", ('Linear Algebra', 4, 2))

cursor.execute("INSERT INTO Students (StudentName, DateOfBirth, Gender, PhoneNumber) VALUES (?, ?, ?, ?)", 
               ('Alice Johnson', '2001-05-15', 'Female', '1234567890'))
cursor.execute("INSERT INTO Students (StudentName, DateOfBirth, Gender, PhoneNumber) VALUES (?, ?, ?, ?)", 
               ('Bob Anderson', '2000-09-20', 'Male', '0987654321'))

cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO Enrollments (StudentID, CourseID) VALUES (?, ?)", (2, 2))

cursor.execute("INSERT INTO Grades (EnrollmentID, Grade) VALUES (?, ?)", (1, 'A'))
cursor.execute("INSERT INTO Grades (EnrollmentID, Grade) VALUES (?, ?)", (2, 'B'))

# Commit and close connection
connection.commit()
connection.close()

print("Database and tables created successfully with sample data!")
