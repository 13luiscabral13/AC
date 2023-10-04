import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the CSV file into a DataFrame
df = pd.read_csv('dataset_edited/players_teams_w_percentages_wo_post.csv')

df = df.loc[:, ~df.columns.str.contains('nname')]


#df['percentage_pointsFromFieldGoal'] = (df['pointsFromFieldGoal'] / df['points']) * 100

#df["percentage_pointsFromFreeThrow"] = (df["ftMade"] / df["points"]) * 100

#df["percentage_pointsFromThree"] = (df["threeMade"] / df["points"]) * 100

df.to_csv('dataset_edited/players_teams_w_percentages_wo_post.csv')