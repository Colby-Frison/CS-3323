import re

# Name: Colby Frison
# OUID: 113568816
# Date: 4/8/2025
# Course: CS 3323
# Assignment: Homework 6
# Description: Processes student records, calculates grades, and generates an HTML report.
#              Grades are assigned as follows: A (top 1/3), B (middle 1/3), F (bottom 10%),
#              C/D (remaining students based on eagerness).

def getStudentData():
    """
    Reads input.txt from either the Homework directory or current directory.
    Returns the file contents or raises FileNotFoundError if not found.
    """
    # First attempt: Look in the Homework/Homework 6 directory
    try:
        with open('input.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found in main directory \n")

        # Second attempt: Look in the current directory
        path = input("Please enter the path to the input.txt file: ")
        try:
            with open(path, 'r') as file:
                return file.read()
        except:
            try:
                path += "/input.txt"
                with open(path, 'r') as file:
                        return file.read()
            except FileNotFoundError:
                raise FileNotFoundError("Could not find input.txt in either directory")

def extractStudentInfo(rawData):
    """
    Parses raw input into structured student records.
    Each record contains: ID, first name, last name, score, and eagerness level.
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
    Processes a single student record into a structured dictionary.
    Extracts ID, names, score, and eagerness level from the input parts.
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
    Assigns grades based on ranking and eagerness:
    - Top n/3: A
    - Next n/3: B
    - Bottom 10%: F
    - Remaining: C (eager) or D (lazy)
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
    Generates an HTML report with two tables:
    1. Final grades sorted alphabetically
    2. Raw data including scores and eagerness levels
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
        /* Base styling for the entire page */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }
        
        /* Container for all content*/
        .container {
            max-width: 800px;
            width: 100%;
            margin: 20px auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Headings styling*/
        h1, h2 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        h1 {
            font-size: 1.8em;
        }
        h2 {
            font-size: 1.4em;
            margin-top: 40px;
            color: #3498db;
        }
        
        /* Table styling */
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
            font-size: 0.9em;
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
        
        /* Grade-specific colors for visual feedback */
        .grade-A { color: #27ae60; font-weight: bold; }  /* Green for A */
        .grade-B { color: #2980b9; font-weight: bold; }  /* Blue for B */
        .grade-C { color: #f39c12; font-weight: bold; }  /* Orange for C */
        .grade-D { color: #e67e22; font-weight: bold; }  /* Dark Orange for D */
        .grade-F { color: #e74c3c; font-weight: bold; }  /* Red for F */
        
        /* Score column styling */
        .score {
            text-align: right;
            font-family: monospace;
        }
        
        /* Eagerness level styling */
        .eagerness-E {
            color: #27ae60;  /* Green for Eager */
            font-weight: bold;
        }
        .eagerness-L {
            color: #e74c3c;  /* Red for Lazy */
            font-weight: bold;
        }
        
        /* info box styling */
        .metadata-box {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 30px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            text-align: center;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        .metadata-box h3 {
            color: #3498db;
            margin-top: 0;
            margin-bottom: 20px;
            text-align: center;
            font-size: 1.2em;
        }
        .metadata-box p {
            margin: 8px 0;
            color: #2c3e50;
            font-size: 0.95em;
            line-height: 1.5;
            text-align: center;
        }
        .metadata-box .label {
            font-weight: 600;
            color: #3498db;
            display: inline-block;
            width: 100px;
            text-align: right;
            margin-right: 10px;
        }
        .metadata-box .value {
            text-align: left;
            display: inline-block;
            min-width: 150px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- metadata section at the top -->
        <div class="metadata-box">
            <p><span class="label">Name:</span><span class="value">Colby Frison</span></p>
            <p><span class="label">OUID:</span><span class="value">113568816</span></p>
            <p><span class="label">Date:</span><span class="value">4/8/2025</span></p>
            <p><span class="label">Course:</span><span class="value">CS 3323</span></p>
            <p><span class="label">Assignment:</span><span class="value">Homework 6</span></p>
        </div>
        
        <!-- Main grades table -->
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
    
    # Add raw data table
    htmlPage += """        </table>
        <h2>Raw Student Data</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Score</th>
                <th>Eagerness</th>
            </tr>
"""
    
    # Add raw data for each student
    for student in sortedStudents:
        eagernessClass = f"eagerness-{student['eagerness']}"
        htmlPage += f"""            <tr>
                <td>{student['id']}</td>
                <td>{student['firstName']}</td>
                <td>{student['lastName']}</td>
                <td class="score">{student['score']}</td>
                <td class="{eagernessClass}">{student['eagerness']}</td>
            </tr>
"""
    
    # Close the HTML document
    htmlPage += """        </table>
    </div>
</body>
</html>"""
    
    return htmlPage

def main():
    """
    Main function that combines all the functions to process the entire grade processing workflow.
    
    This function:
    1. Reads the input file
    2. Parses student records
    3. Calculates grades
    4. Generates the HTML output
    5. Saves the results to output.html

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
        with open('output.html', 'w') as file:
                file.write(gradeReport)
            
        print("Successfully generated output.html")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 