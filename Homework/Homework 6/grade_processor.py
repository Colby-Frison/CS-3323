import re

# Name: Colby Frison
# OUID: 113568816
# Date: 4/8/2025
# Course: CS 3323
# Assignment: Homework 6

# Description: This program processes student records from input.txt, calculates grades based on
#              specific rules, and generates an HTML table displaying the results. The grading
#              system assigns A's to the top third, B's to the middle third, F's to the bottom
#              10%, and C's/D's to the remaining students based on their eagerness level.


def getStudentData():
    """
    Reads and returns the contents of input.txt.
    
    This function attempts to locate and read the input file containing student records.
    It first checks the Homework/Homework 6 directory, then falls back to the current
    directory if the file is not found. This ensures the program can find the input
    file regardless of where it is run from.
    
    """
    # First attempt: Look in the Homework/Homework 6 directory
    try:
        with open('Homework/Homework 6/input.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        # Second attempt: Look in the current directory
        try:
            with open('input.txt', 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Could not find input.txt in Homework/Homework 6 directory or current directory")

def extractStudentInfo(rawData):
    """
    Parses the raw input content into structured student records.
    
    This function processes the input string to extract individual student records.
    Each record contains: ID number, first name, last name, score, and eagerness level.
    The function handles records that may span multiple lines and cleans up any extra
    whitespace or newlines in the input.
    
    """
    # Clean up the input by removing extra spaces and newlines
    cleanData = ' '.join(rawData.split())
    
    # Initialize lists to store student info
    allStudents = []
    currentStudent = []
    
    # Split the content into individual words for processing
    words = cleanData.split()
    position = 0
    while position < len(words):
        # Check if current word is a 9-digit number (ID)
        currentWord = words[position]
        if len(currentWord) == 9 and currentWord.isdigit():
            # If we have a previous student, process them before starting a new one
            if currentStudent:
                addStudentToList(currentStudent, allStudents)
                currentStudent = []
            currentStudent.append(currentWord)  # Add the ID number
            position += 1
        else:
            currentStudent.append(currentWord)
            position += 1
    
    # Don't forget to process the last student
    if currentStudent:
        addStudentToList(currentStudent, allStudents)
    
    return allStudents

def addStudentToList(studentParts, studentList):
    """
    Processes a single student record from its component parts.
    
    This helper function takes the raw parts of a student record and extracts
    the relevant information: ID, names, score, and eagerness level. It handles
    the parsing of names and ensures all required fields are present.

    """
    # The first part is always the 9-digit ID number
    studentId = studentParts[0]
    
    # Find where the score is (first number after the names)
    scorePosition = 0
    for index, part in enumerate(studentParts[1:], 1):
        if part.isdigit():
            scorePosition = index
            break
    
    # Get the student's names (everything between ID and score)
    nameParts = studentParts[1:scorePosition]
    # The first name is the first part after the ID
    firstName = nameParts[0]
    # The last name is the second part after the ID
    lastName = nameParts[1] if len(nameParts) > 1 else ""
    
    # Get the student's score and participation level
    finalScore = int(studentParts[scorePosition])
    participation = studentParts[scorePosition + 1]
    
    # Create and add the student's record
    studentList.append({
        'id': studentId,
        'firstName': firstName,
        'lastName': lastName,
        'score': finalScore,
        'eagerness': participation
    })

def assignGrades(studentRecords):
    """
    Calculates letter grades for all students based on the specified rules.
    
    The grading rules are:
    1. Top n/3 students receive grade A
    2. Next n/3 students receive grade B
    3. Bottom n/10 students receive grade F
    4. Remaining students receive grade C if eager, D if lazy
    
    """
    totalStudents = len(studentRecords)
    if totalStudents < 7:
        raise ValueError("Need at least 7 students")
    
    # Lambda function explanation:
    # key=lambda student: (-student['score'], 0 if student['eagerness'] == 'E' else 1)
    # This sorts students by score (descending) and eagerness
    # -student['score'] makes higher scores come first (descending order)
    # The second part (0 if 'E' else 1) makes 'E' students come before 'L' students when scores are equal
    rankedStudents = sorted(studentRecords, key=lambda student: (-student['score'], 0 if student['eagerness'] == 'E' else 1))
    
    # Calculate the cutoffs for each grade category
    aCutoff = totalStudents // 3  # Top third get A
    bCutoff = 2 * (totalStudents // 3)  # Next third get B
    fCutoff = totalStudents - (totalStudents + 9) // 10  # Bottom 10% get F
    
    # Assign grades based on position in ranked list
    for rank, student in enumerate(rankedStudents):
        if rank < aCutoff:
            student['grade'] = 'A'
        elif rank < bCutoff:
            student['grade'] = 'B'
        elif rank >= fCutoff:
            student['grade'] = 'F'
        else:
            student['grade'] = 'C' if student['eagerness'] == 'E' else 'D'
    
    return rankedStudents

def createGradeReport(studentsWithGrades):
    """
    Generates an HTML table displaying student records and their grades.
    
    Creates a well-formatted HTML table with student information sorted by
    last name, first name, and ID number. Includes modern CSS styling for
    a professional presentation.
    """
    # Lambda function explanation:
    # key=lambda student: (student['lastName'], student['firstName'], student['id'])
    # This sorts students alphabetically by last name, then first name, then ID
    # The tuple (lastName, firstName, id) ensures proper alphabetical sorting
    sortedStudents = sorted(studentsWithGrades, key=lambda student: (student['lastName'], student['firstName'], student['id']))
    
    # Start building the HTML document
    htmlPage = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Grades Report</title>
    <style>
        /* Modern styling for the table */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #3498db;
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        td {
            color: #2c3e50;
        }
        .grade-A { color: #27ae60; font-weight: bold; }
        .grade-B { color: #2980b9; font-weight: bold; }
        .grade-C { color: #f39c12; font-weight: bold; }
        .grade-D { color: #e67e22; font-weight: bold; }
        .grade-F { color: #e74c3c; font-weight: bold; }
        .metadata-box {
            margin-top: 30px;
            padding: 15px;
            border-radius: 4px;
        }
        .metadata-box p {
            margin: 5px 0;
            color: #2c3e50;
            font-size: 1em;
        }
        .metadata-box .label {
            font-weight: 600;
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Grades Report</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Grade</th>
            </tr>
"""
    
    # Add each student's information as a table row
    for student in sortedStudents:
        gradeClass = f"grade-{student['grade']}"
        htmlPage += f"""            <tr>
                <td>{student['id']}</td>
                <td>{student['firstName']}</td>
                <td>{student['lastName']}</td>
                <td class="{gradeClass}">{student['grade']}</td>
            </tr>
"""
    
    # Add metadata box
    htmlPage += """        </table>
        <div class="metadata-box">
            <p><span class="label">Name:</span> Colby Frison</p>
            <p><span class="label">OUID:</span> 113568816</p>
            <p><span class="label">Date:</span> 4/8/2025</p>
            <p><span class="label">Course:</span> CS 3323</p>
            <p><span class="label">Assignment:</span> Homework 6</p>
        </div>
    </div>
</body>
</html>"""
    
    return htmlPage

def main():
    """
    Main function that orchestrates the entire grade processing workflow.
    
    This function:
    1. Reads the input file
    2. Parses student records
    3. Calculates grades
    4. Generates the HTML output
    5. Saves the results to output.html
    
    Handles any errors that might occur during the process and provides
    appropriate error messages.
    """
    try:
        # Read and process the input file
        rawData = getStudentData()
        studentRecords = extractStudentInfo(rawData)
        
        # Calculate grades for all students
        gradedStudents = assignGrades(studentRecords)
        
        # Generate the HTML output
        gradeReport = createGradeReport(gradedStudents)
        
        # Save the output file
        try:
            with open('Homework/Homework 6/output.html', 'w') as file:
                file.write(gradeReport)
        except:
            # Fallback to current directory if needed
            with open('output.html', 'w') as file:
                file.write(gradeReport)
            
        print("Successfully generated output.html")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 