import pandas as pd
import sys
from subprocess import run
user_input = input("Enter the path of the dataset ")
df = pd.read_csv(user_input)

describing=df.describe()
insight_1 = describing.to_string()
with open('eda_insight_1.txt', 'w') as file:
    file.write(insight_1)

# In[12]:


female_distribution = df["Gender_female"].value_counts()
male_distribution = df["Gender_male"].value_counts()
male_str = str(male_distribution)
female_str= str (female_distribution)



insight_2 = female_str
with open('eda_insight_2.txt', 'w') as file:
    file.write(insight_2)

insight_3 = male_str
with open('eda_insight_3.txt', 'w') as file:
    file.write(insight_3)


# In[13]:


male_distribution
female_distribution


# In[14]:


#value indicates the shape of the distribution's tails. A positive value suggests heavier tails (more outliers),
#and a negative value suggests lighter tails compared to a normal distribution.

age_kurtosis = df["Age"].kurt()


# In[15]:


age_kurtosis


run(["python", "vis.py", user_input])