import pandas as pd

df = pd.read_csv('combinedData.csv')

# Use the value_counts() function to count the occurrences of 'N' and 'Y' in the 'playoff' column
playoff_counts = df['playoff'].value_counts()

# Get the count of 'N' and 'Y' values
count_N = playoff_counts.get('N', 0)
count_Y = playoff_counts.get('Y', 0)

# Print the counts
print(f"Count of 'N': {count_N}")
print(f"Count of 'Y': {count_Y}")