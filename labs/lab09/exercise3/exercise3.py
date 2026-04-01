import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):

# Load data
    df = pd.read_csv(filename)

    # Plot Math scores using DataFrame column
    plt.plot(df.index, df['Math'])

    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Scores Trends")

    plt.show()

    return len(df)

result = show_math_trend("labs/lab09/data/students.csv")

