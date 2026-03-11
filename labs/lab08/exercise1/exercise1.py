# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    
    f_in = open(input_file, "r")
    lines = f_in.readlines()
    f_in.close()

    f_out = open(output_file, "w")

    count = 0

    for i in range(0, len(lines), 2):
        student_id
    

    

# Test your code here
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
