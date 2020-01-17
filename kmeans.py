import random as random
data=[]
clusters=[]
means=[]
k=1

def init_data():
 global data
 data=list(map(float,input().split(" ")))

def init_cluster_size():
 global k
 k= int(input())
 print ("Cluster size:",k)
 global clusters
 clusters=[[] for i in range(k)]

#returns the mean of that cluster
def clusterMean(cluster):
 
 size= len(cluster)
 print("cluster is:",cluster)
 print("sum is:",sum(cluster), " avaerage:", sum(cluster)/size) 
 return sum(cluster)/size

def updateMeans():
 
 global k
 global means
 global clusters
 
 for i in range(k):
  means[i]=clusterMean(clusters[i])
 print("new means:",means)
 
#function to calculate euclidean distance for all means and return the index of mean that's closest
def closestMean(m,elm):
 
 min_d=[]
 for i in range(len(m)):
  min_d.append(abs(m[i]-elm))
 print("Min distance array is:",min_d, "elm is:",elm)
 min_ind= min_d.index(min(min_d))
 print("Closest index is:",min_ind)
 return min_ind
 
def updateCluster(means,data):
 global k
 newClusters=[ [] for i in range(k) ]
 print(newClusters)
 for d in data:
  newClusters[closestMean(means,d)].append(d)
 print("After init:",newClusters)
 return newClusters
 
def kmeans():
 global k
 global data
 global clusters
 global means
 
 print("Enter 1-D data")
 init_data()
 
 print("Enter no of clusters:")
 init_cluster_size()
 
 #pick random elements
 means=random.sample(data,k)
 print("random means:",means)
 
 newClusters=[]
 i=0
 while True:
  print ("#",i)
  
  clusters=updateCluster(means,data)
  updateMeans()
  newClusters= updateCluster(means,data)
  if newClusters==clusters:
   break
  else:
   i+=1
 clusters= newClusters
 print("Final cluster:",clusters)
 print ("Final means:",means)
 
#closestMean([2,9,3],2)
#updateCluster([2,9,3],[1,2,3,4,5,6,7,8,9])
kmeans()
 
 

