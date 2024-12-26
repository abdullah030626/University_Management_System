CREATE DATABASE UniversityManagementSystem;

-- Students Table
CREATE TABLE Students (
    StudentID INT IDENTITY(1,1) PRIMARY KEY,
    StudentName NVARCHAR(100) NOT NULL,
    DateOfBirth DATE,
    Gender NVARCHAR(10),
    PhoneNumber NVARCHAR(15)
);

-- Courses Table
CREATE TABLE Courses (
    CourseID INT IDENTITY(1,1) PRIMARY KEY,
    CourseName NVARCHAR(100) NOT NULL,
    Credits INT NOT NULL,
    InstructorID INT NOT NULL
);

-- Faculty Table
CREATE TABLE Faculty (
    FacultyID INT IDENTITY(1,1) PRIMARY KEY,
    FacultyName NVARCHAR(100) NOT NULL,
    Department NVARCHAR(100)
);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT IDENTITY(1,1) PRIMARY KEY,
    StudentID INT NOT NULL FOREIGN KEY REFERENCES Students(StudentID),
    CourseID INT NOT NULL FOREIGN KEY REFERENCES Courses(CourseID),
    EnrollmentDate DATE NOT NULL DEFAULT GETDATE()
);

-- Grades Table
CREATE TABLE Grades (
    GradeID INT IDENTITY(1,1) PRIMARY KEY,
    EnrollmentID INT NOT NULL FOREIGN KEY REFERENCES Enrollments(EnrollmentID),
    Grade NVARCHAR(2)
);

-- Insert into Faculty
INSERT INTO Faculty (FacultyName, Department)
VALUES ('Dr. John Smith', 'Computer Science'), 
       ('Dr. Emily Brown', 'Mathematics');

-- Insert into Courses
INSERT INTO Courses (CourseName, Credits, InstructorID)
VALUES ('Introduction to Programming', 3, 1), 
       ('Linear Algebra', 4, 2);

-- Insert into Students
INSERT INTO Students (StudentName, DateOfBirth, Gender, PhoneNumber)
VALUES ('Alice Johnson', '2001-05-15', 'Female', '1234567890'), 
       ('Bob Anderson', '2000-09-20', 'Male', '0987654321');

-- Insert into Enrollments
INSERT INTO Enrollments (StudentID, CourseID)
VALUES (1, 1), 
       (2, 2);

-- Insert into Grades
INSERT INTO Grades (EnrollmentID, Grade)
VALUES (1, 'A'), 
       (2, 'B');

