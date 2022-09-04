import pandas as pd

#Visualising the dataset
def load_data(dataset,col_names):
    df = pd.read_csv(dataset,delimiter="\t",names=col_names)
    return df

#Visualizing duplicates
def view_data(df):
    dupes = df['url'].value_counts().sort_values(ascending=False)
    print(dupes.head())


