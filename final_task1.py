import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

exams = pd.read_csv('exams.csv')

# define a function to group students by gender and group
def group_students():
    """
    

    Returns
    -------
    list
        DESCRIPTION.

    """
    girls = exams[exams['gender'] == 'female']
    boys = exams[exams['gender'] == 'male']
    girlsA = girls[girls['race/ethnicity'] == 'group A']
    boysA = boys[boys['race/ethnicity'] == 'group A']
    girlsB = girls[girls['race/ethnicity'] == 'group B']
    boysB = boys[boys['race/ethnicity'] == 'group B']
    girlsC = girls[girls['race/ethnicity'] == 'group C']
    boysC = boys[boys['race/ethnicity'] == 'group C']
    girlsD = girls[girls['race/ethnicity'] == 'group D']
    boysD = boys[boys['race/ethnicity'] == 'group D']
    girlsE = girls[girls['race/ethnicity'] == 'group E']
    boysE = boys[boys['race/ethnicity'] == 'group E']
    return [len(girlsA), len(boysA), len(girlsB), len(boysB), len(girlsC), len(boysC), len(girlsD), len(boysD), len(girlsE), len(boysE)]

# call the group_students function to get the number of students for each group and gender
students_per_group = group_students()

# extract the x-axis labels from the original dataframe
groups = exams['race/ethnicity'].unique()

# split the students_per_group list into separate lists for girls and boys
Ygirls = students_per_group[::2]
Zboys = students_per_group[1::2]

# create the bar plot
X_axis = np.arange(len(groups))
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys')
plt.xticks(X_axis, groups)
plt.xlabel("Group")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group and gender")
plt.legend()
plt.show()
