import re
import os

def read_input_file():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    
    with open(input_path, 'r') as file:
        content = file.read()
    return content

def parse_student_records(content):
    # Regular expression to match student records
    pattern = r'(\d{9})\s+([A-Za-z]+)\s+([A-Za-z]+)\s+(\d+)\s+([EL])(?:\s+([A-Za-z\s]+))?'
    records = []
    
    # Find all matches
    matches = re.finditer(pattern, content)
    for match in matches:
        id_num = match.group(1)
        first_name = match.group(2)
        last_name = match.group(3)
        score = int(match.group(4))
        eagerness = match.group(5)
        records.append({
            'id': id_num,
            'first_name': first_name,
            'last_name': last_name,
            'score': score,
            'eagerness': eagerness
        })
    
    return records

def calculate_grades(records):
    n = len(records)
    if n < 7:
        raise ValueError("There must be at least 7 students")
    
    # Sort records by score (descending) and eagerness (E > L)
    sorted_records = sorted(records, 
                          key=lambda x: (-x['score'], 0 if x['eagerness'] == 'E' else 1))
    
    # Calculate grade boundaries
    a_boundary = n // 3
    b_boundary = 2 * (n // 3)
    f_boundary = n - (n + 9) // 10  # n - ceil(n/10)
    
    # Assign grades
    for i, record in enumerate(sorted_records):
        if i < a_boundary:
            record['grade'] = 'A'
        elif i < b_boundary:
            record['grade'] = 'B'
        elif i >= f_boundary:
            record['grade'] = 'F'
        else:
            record['grade'] = 'C' if record['eagerness'] == 'E' else 'D'
    
    return sorted_records

def generate_html(records):
    # Sort by last name, first name, and ID
    sorted_records = sorted(records, 
                          key=lambda x: (x['last_name'], x['first_name'], x['id']))
    
    html =  """ <!DOCTYPE html>
                <html>
                <head>
                    <title>Student Grades</title>
                </head>
                <body>
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Last Name</th>
                            <th>First Name</th>
                            <th>Grade</th>
                        </tr>
                """
    
    for record in sorted_records:
        html += f"""        <tr>
            <td>{record['id']}</td>
            <td>{record['last_name']}</td>
            <td>{record['first_name']}</td>
            <td>{record['grade']}</td>
        </tr>
"""
    
    html += """    </table>
</body>
</html>"""
    
    return html

def main():
    try:
        content = read_input_file()
        records = parse_student_records(content)
        graded_records = calculate_grades(records)
        html = generate_html(graded_records)
        
        # Save output.html in the same directory as the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, 'output.html')
        
        with open(output_path, 'w') as file:
            file.write(html)
            
        print("Successfully generated output.html")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 