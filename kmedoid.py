"""
Code by DG
K -Medoid for one-D data on any general k
"""
import random as random
dataset=[]
min_distance=[]
clusters=[]
k=1
def init_dataset():
  global dataset
  dataset=list(map(float,input("Enter 1D dataset:").split()))

def init_k():
  global k
  global clusters
  k=int(input("Enter cluster size:"))
  clusters=[ [] for i in range(k)] 
#outputs the distance and closer element from representative object list
def distance(elm, objs):
  ans=[abs(elm-objs[0]),0] #store min distance and close elm index
  
  for obj in objs:
    dist= abs(obj-elm)
    if dist<ans[0]:
      ans[0]=dist
      ans[1]= objs.index(obj)
      #print("Updated the distance:%d and index to:%d elm:%d"%(ans[0],ans[1],elm))
  return ans

def calculate_s(min_distance):
  return sum(min_distance)/len(min_distance)

def kmedoid():
  global dataset
  global k
  global min_distance
  global clusters
  
  init_dataset()
  init_k()
  old_s=None
  new_s=None
  new_clusters=list(clusters)
  
  objs=random.sample(dataset,2*k) #first half are representative obj and second half non-reprensentative
  
  rep_obj= objs[:k]
  non_rep_obj=objs[k:]
  
  for d in dataset:
    res=distance(d,rep_obj)
    min_distance.append(res[0])
    clusters[res[1]].append(d)
  
  print("clusters:",clusters)
    
  old_s=calculate_s(min_distance)
  print("S:",old_s," for rep_obj:",rep_obj)
  
  while new_s==None or (new_s-old_s)<0:
    min_distance=[]
    new_clusters=[[] for d in range(k)]
    for d in dataset:
     res=distance(d,non_rep_obj)
     min_distance.append(res[0])
     new_clusters[res[1]].append(d)
    
    print("New clusters:",clusters)
    
    new_s=calculate_s(min_distance)
    print("New S:",new_s," for non_rep_obj:",non_rep_obj)
    
    if new_s-old_s<0:
      clusters= list(new_clusters)
      old_s= new_s
      rep_obj= list(non_rep_obj)
      print("updated the rep obj with non-rep-obj")  
      non_rep_obj=random.sample(dataset,k)
    else:
      break
      
  print ("Final clusters:",clusters)  
   
 
    
  
kmedoid()
