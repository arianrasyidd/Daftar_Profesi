import numpy as np
import pandas as pd

df = pd.read_csv('profesi.csv', sep='|')
print(df)

occup = df['occupation'].value_counts()
print(len(occup))
print(occup.index.tolist())

dfa = df.groupby([df['occupation'],df['gender']]).describe()
dfa = dfa['age'][['max','min','mean']]
dfa.rename(columns={'max':'max_usia','min':'min_usia','mean':'rerata_usia'},inplace=True)
print(dfa)

gender = pd.crosstab(df.occupation, df.gender).apply(lambda i : i / i.sum(), axis= 1) * 100
gender['%total'] = gender['F']+gender['M']
gender.rename(columns={'F':'%female','M':'%male'},inplace=True)
gender = gender[['%male','%female','%total']]
print(gender)