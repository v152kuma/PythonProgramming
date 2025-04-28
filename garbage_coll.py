#referenceCount and gcColletion in python

arr =[1,2,3] #refcount =1

copy_arr = arr #refcount = 2
 
arr =[4,5,6] # refcount = 1

del copy_arr #refcount = 0 #automatic garbage collection

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

#create two nodes
a = Node(1)
b = Node(2)

a.next = b
b.next = a

del a
del b

#but the nodes are still referencing each other

import gc

gc.collect()

#force python to clean up circular references


