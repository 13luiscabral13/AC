import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file into a DataFrame
df = pd.read_csv('dataset_edited/players_teams_w_percentages_wo_post.csv')

numeric_columns = ["GP","GS","dq","mpg","ppg","apg","rpg","spg","bpg","topg","pfpg","fg%","3p%","ft%", "percentage_pointsFromFieldGoal", "percentage_pointsFromFreeThrow", "percentage_pointsFromThree"]

# Calculate the correlation matrix
correlation_matrix = df[numeric_columns].corr()

# Create a heatmap with Seaborn
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.8)
plt.title("Correlation Matrix Heatmap")
plt.savefig("prntscrns/graphs/correlation_matrix_simplified.png")