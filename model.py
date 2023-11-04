import pandas as pd
from sklearn.cluster import KMeans


user_input = input("Enter the path of the dataset ")
df = pd.read_csv(user_input)



columns_to_drop = ["Name","AgeGroup","FareCategory","Cabin","Ticket"]
df.drop(columns_to_drop, axis=1, inplace=True)

#D_new

k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=0)
df['cluster'] = kmeans.fit_predict(df)

cluster_counts = df['cluster'].value_counts().sort_index()

cluster_string = cluster_counts.astype(str)


with open('k.txt', 'w') as file:
    for cluster, count in enumerate(cluster_string):
        file.write(f'Cluster {cluster}: {count} records\n')
