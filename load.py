import pandas as pd
import sys
from subprocess import run
user_input = input("Enter the path of the dataset ")
def read_dataset(user_input):
    df = pd.read_csv(user_input)
    return df


df=read_dataset(user_input)

print(df)



run(["python", "dpre.py", user_input])