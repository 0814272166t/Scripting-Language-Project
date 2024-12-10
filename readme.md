# Scripting Assignment

## Objective

Create a Student Grade Book program that manages and displays students' grades using different Python data types.

## Instructions

### 1. Grade Book Setup

- Use a dictionary to store the information for each student, with the student ID (string) as the key.
- The value for each student should be a list that includes:
  - **Name (string):** The student’s full name.
  - **Grades (list of floats):** A list containing grades for five subjects.

### 2. Student Data Entry

- Manually populate the dictionary with information for at least 3 students, each with a unique student ID, name, and a list of five grades. Use a mix of integer and float values for the grades.

### 3. Data Manipulation Tasks

- **Update Grade:** Modify a specific grade for a student by locating their student ID and changing the grade at a specific position in the list.
- **Add New Student:** Add a new student’s data (ID, name, and grades) directly into the dictionary.
- **Remove Student:** Remove a student’s data from the dictionary by their ID.

### 4. Display Grades

- Format and print each student’s name, ID, and grades using string formatting.
- Display the highest and lowest grade for each student.

### 5. Class Average Calculation

- Calculate and display the average grade for each student across all subjects.
- Calculate and display the class average for each subject (i.e., the average of each subject's grades across all students).

### 6. Comparison Operations

- Compare each student’s average grade to the class average.
- Print a message indicating whether each student’s average is above, below, or equal to the class average.
