# -*- coding: utf-8 -*-
"""python project salary

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c-q9z2PT6XR6FVHBwV2bAYiD6AJuX8ju
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salarydataset = pd.read_csv("/content/salary_prediction_data (1).csv")
df=pd.DataFrame(salarydataset)

salarydataset.info()

plt.scatter(salarydataset['Experience'], salarydataset['Salary'], c=salarydataset['Experience'], cmap = 'plasma')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('Experience vs Salary')
plt.show()

plt.scatter(salarydataset['Age'], salarydataset['Salary'], c=salarydataset['Age'], cmap = 'plasma')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()

avg_salary = df.groupby('Gender')['Salary'].mean()
plt.figure(figsize = (3,5))
plt.bar(avg_salary.index, avg_salary.values, color = 'lightgreen')
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.show()

avg_salary = df.groupby('Job_Title')['Salary'].mean()

plt.figure(figsize=(5, 5))
plt.bar(avg_salary.index, avg_salary.values, color='skyblue')

plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.show()