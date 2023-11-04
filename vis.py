import pandas as pd
from subprocess import run
from matplotlib import pyplot as plt 
import seaborn as sns
import sys
from subprocess import run


user_input = input("Enter the path of the dataset ")
df = pd.read_csv(user_input)


numeric_columns = df.select_dtypes(include='number')

# Compute the correlation matrix
correlation_matrix = numeric_columns.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Between Numeric Columns')
plt.show()
plt.savefig('vis.png')

run(["python", "model.py", user_input])