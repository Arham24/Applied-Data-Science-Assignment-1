import pandas as pd
import matplotlib.pyplot as plt

def line_plot(csv_file, x_col, y_cols, title, x_label, y_label):
    # Load data
    data = pd.read_csv('london_weather.csv')

    # Extract relevant data
    x = data[x_col]
    ys = [data[col] for col in y_cols]

    # Create plot
    for y, label in zip(ys, y_cols):
        plt.plot(x, y, label=label)

    # Add labels and legend
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()

    # Show plot
    plt.show()

# Call the function with your desired arguments
line_plot('london_weather.csv', 'date', ['min_temp', 'max_temp'], 'Weather on London', 'Date', 'Value')
