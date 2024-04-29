import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = './Book1.xlsx'  # Replace with the path to your Excel file
data = pd.read_excel(file_path)

# Convert the 'is covered' column from Yes/No to 1/0
data['is covered'] = data['is covered'].map({'Yes': 1, 'yes': 1, 'No': 0, 'no': 0})

# Calculate the average coverage for each line of code
average_data = data.groupby('lines')['is covered'].mean().reset_index()

# Plotting the average coverage for each line of code
plt.figure(figsize=(12, 7))
plt.scatter(average_data['lines'], average_data['is covered'], alpha=0.5)

# Adjusting the x-axis to accommodate the full range of 'lines'
plt.xlim(average_data['lines'].min(), average_data['lines'].max())

plt.title('Average Coverage by Lines of Code')
plt.xlabel('Lines of Code')
plt.ylabel('Average Coverage (0=False, 1=True)')
plt.grid(True)
plt.show()
