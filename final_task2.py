import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
exams = pd.read_csv('exams.csv')

# Group the data by gender and group and calculate the count for each group
grouped_data = exams.groupby(['gender', 'race/ethnicity']).size()

# Separate the data by gender
male_data = grouped_data['male']
female_data = grouped_data['female']

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2)

# Create a pie chart for male data in the first subplot
axs[0].pie(male_data.values, labels=male_data.index, autopct='%1.0f%%', startangle=90)
axs[0].set_title('Male Students by Groups')

# Create a pie chart for female data in the second subplot
axs[1].pie(female_data.values, labels=female_data.index, autopct='%1.0f%%', startangle=90)
axs[1].set_title('Female Students by Groups')

# Adjust the layout and spacing between subplots
fig.tight_layout(pad=3)

# Display the plot
plt.show()
