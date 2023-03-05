import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("exams.csv")

# Create a histogram for each subject using subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

axs[0].hist(df["math score"])
axs[0].set_xlabel("Math Score")
axs[0].set_ylabel("Frequency")
axs[0].set_title("Distribution of Math Scores")

axs[1].hist(df["reading score"])
axs[1].set_xlabel("Reading Score")
axs[1].set_ylabel("Frequency")
axs[1].set_title("Distribution of Reading Scores")

axs[2].hist(df["writing score"])
axs[2].set_xlabel("Writing Score")
axs[2].set_ylabel("Frequency")
axs[2].set_title("Distribution of Writing Scores")

# Display the plot
plt.show()
