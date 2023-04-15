from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
df = pd.read_csv("Mall_Customers.csv")
print(df)
df.head()
plt.scatter(df.Age,df['Annual_Income_(k$)'])
plt.xlabel('Spending_Score')
plt.ylabel('Annual_Income_(k$)')
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Spending_Score','Annual_Income_(k$)']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]
plt.scatter(df1.Age,df1['CustomerID'],color='green')
plt.scatter(df2.Age,df2['Genre'],color='red')
plt.scatter(df3.Age,df3['Age'],color='brown')
plt.scatter(df4.Age,df4['Annual_Income_(k$)'],color='yellow')
plt.scatter(df5.Age,df5['Spending_Score'],color='blue')
plt.scatter(km.cluster_centers_[:,1],km.cluster_centers_[:,0],color='pink',marker='*',label='centroid')
plt.xlabel('Spending_Score')
plt.ylabel('Annual_Income_(k$)')
plt.legend()
scaler = MinMaxScaler()

scaler.fit(df[['Annual_Income_(k$)']])
df['Annual_Income_(k$)'] = scaler.transform(df[['Annual_Income_(k$)']])

scaler.fit(df[['Spending_Score']])
df['Spending_Score'] = scaler.transform(df[['Spending_Score']])
df.head()
plt.scatter(df.Age,df['Annual_Income_(k$)'])
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Spending_Score','Annual_Income_(k$)']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Spending_Score','Annual_Income_(k$)']])
    sse.append(km.inertia_)

plt.xlabel('Age')
plt.ylabel('Annual_Income_(k$)')
plt.show()
plt.plot(k_rng,sse)
