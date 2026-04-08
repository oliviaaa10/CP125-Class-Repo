import pandas as pd
import matplotlib.pyplot as plt


def plot_subject_maximums(filename):
    df = pd.read_csv(filename)

    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]
    max_scores = [df[sub].max() for sub in subjects]

    plt.figure(figsize=(8,5))
    plt.plot(subjects, max_scores, marker='o', color='blue', linestyle='-')
    plt.title("Maximum Scores by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")

    plt.grid(True)
    plt.show()

    total_students = len(df)
    

    return total_students 

count = plot_subject_maximums("labs/lab09/data/students.csv")
print(count)

    
