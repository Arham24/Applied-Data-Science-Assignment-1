import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("exams.csv")

# Create a line plot for each subject using subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 5))

df.plot(kind="line", x="math score", y="student id", ax=axs[0])
axs[0].set_xlabel("Math Score")
axs[0].set_ylabel("Student ID")
axs[0].set_title("Math Scores")


"Arham"
df.plot(kind="line", x="reading score", y="student id", ax=axs[1])
axs[1].set_xlabel("Reading Score")
axs[1].set_ylabel("Student ID")
axs[1].set_title("Reading Scores")

df.plot(kind="line", x="writing score", y="student id", ax=axs[2])
axs[2].set_xlabel("Writing Score")
axs[2].set_ylabel("Student ID")
axs[2].set_title("Writing Scores")

# Display the plot
plt.show()
