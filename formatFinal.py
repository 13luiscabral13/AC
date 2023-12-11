import pandas as pd

df = pd.read_csv('predictions/svm_predictions.csv')

df = df.drop(columns=['Unnamed: 0', 'confID_EA', 'certainty'])

# in playoff column, change 1 to Y and 0 to N
df['playoff'] = df['playoff'].replace(1, 'Y')
df['playoff'] = df['playoff'].replace(0, 'N')

# in tmID column, change DET to TUL, SAS to UTA and ORL to CON
df['tmID'] = df['tmID'].replace('DET', 'TUL')
df['tmID'] = df['tmID'].replace('UTA', 'SAS')
df['tmID'] = df['tmID'].replace('ORL', 'CON')

# sort by tmID
df = df.sort_values(by=['tmID'])

# remove index column
df = df.reset_index(drop=True)

df.to_csv('final_predictions.csv')