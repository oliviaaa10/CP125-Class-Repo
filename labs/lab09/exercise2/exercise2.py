import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)

    math_average = round(df["Math"].mean(), 1)
    science_average = round(df["Science"].mean(), 1)
    english_average = round(df["English"].mean(), 1)

    averages = {
        "Math": math_average,
        "Science": science_average,
        "English": english_average
    }

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    averages["best_subject"] = best_subject
    averages["worst_subject"] = worst_subject

    return averages


result = compare_averages("labs/lab09/data/students.csv")
print(result)