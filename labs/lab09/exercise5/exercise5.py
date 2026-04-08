import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename)

    filtered_df = df[ (df["Math"] > 85) & (df["Science"] > 85) & (df["English"] > 85) & (df["Physics"] > 85) & (df["Chemistry"] > 85)]

    names = set(filtered_df["Name"])
    count = len(names)

    result = { "count" : count,
              "names" : names 
    }

    return result

result = high_performers("labs/lab09/data/students.csv")
print(result)

