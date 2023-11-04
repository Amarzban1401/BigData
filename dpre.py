import pandas as pd
import sys
from subprocess import run
user_input = input("Enter the path of the dataset ")
df = pd.read_csv(user_input)

df.isnull().sum()


# In[4]:


df = df.dropna(subset=["Age", "Embarked" , "Cabin"])


# In[5]:


df['Age'].fillna((df['Age'].mean()),inplace=True)


# In[6]:


df


# In[7]:


df.isnull().sum()


# In[8]:


df["FamilySize"] = df["SibSp"] + df["Parch"]


# In[9]:


df=pd.get_dummies(df,columns=['Pclass','Gender','Embarked'])

age_bins = [0, 18, 65, 100]
age_labels = ['Child', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

fare_bins = [0, 10, 50, 600]
fare_labels = ['Low', 'Medium', 'High']
df['FareCategory'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels,)



df


df.to_csv('res_dpre.csv', index=False)

run(["python", "eda.py", user_input])