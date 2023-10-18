import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# Load the CSV file into a DataFrame
df = pd.read_csv('dataset_edited/new_tester.csv')


# Get a list of unique positions
positions = df['pos'].unique()

# Create a list of colors for the histograms
colors = ['red', 'green', 'purple', 'orange', 'black', 'pink', 'cyan', 'lavender', 'lime', 'indigo']
# Create a single plot with 5 histograms, each corresponding to a position
plt.figure(figsize=(10, 6))

for i, position in enumerate(positions):
    position_data = df[df['pos'] == position]
    #plt.hist(position_data['ppm'], bins=20, color=colors[i], label=position, alpha=0.5, density=True)
    sns.kdeplot(position_data['ppm'], color=colors[i], label=position+' density', zorder=2)

plt.title('Histograms of PPM for Different Positions')
plt.xlabel('PPM')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.savefig('density_for_ppm')
plt.show() # HISTOGRAM FOR EVERY POSITION





