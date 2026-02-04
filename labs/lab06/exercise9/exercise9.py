def find_qualified_students(student_records, required_courses):
    qualified = []
    
    for student_id, completed in student_records:
        common = required_courses - completed
        
        if common == set():
            qualified.append(student_id)
    
    return sorted(qualified)


student_records = [
    ("S1", {"Math", "Physics"}),
    ("S2", {"Math"})
]

required_courses = {"Math", "Physics"}

qualified_students = find_qualified_students(student_records, required_courses)
print(qualified_students)

