# Name : Olivia Polus
# Write a Python program that checks the grade for one student.

def determine_grade(mark):
    mark = int(input("Enter the students mark :"))
    print(f"Enter the students mark : {mark}")

    if mark >= 80 :
        grade = "A"
    elif mark >= 60 and mark <= 79 :
        grade = "B"
    elif mark >= 50 and mark <= 59 :
        grade = "C"
    elif mark >= 40 and mark <=49 :
        grade = "G" 
    else :
        grade = "F"
    
    return grade


result = determine_grade()
print(f"Mark : {mark}, Grade : {result} ")