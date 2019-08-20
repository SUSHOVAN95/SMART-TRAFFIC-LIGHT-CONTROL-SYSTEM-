from collections import namedtuple


# A simple implementation of Priority Queue 
# using Queue. 
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 

Pair = namedtuple("Pair", ["first", "second"]) #for making pair of two element


#initialization
tmax=90                         # maximum allowed time interval for green signal

a=0.05                          # startup delay (used for bias)

stf=[0.41,0.41,0.41,0.41]       #traffic flow speed in terms of no of vehichle crossing an intersection per sec (found by statistical annalysis)

comp=[2,3,0,1]                  # complementary lane no for each lane 

carcount=[0,0,0,0]              # array for storing car count of each lane

visit=[0,0,0,0]                 # visited array required to stop starvation

q = PriorityQueue()             # initialize a priority queue

# function for calculating time to be assigned for the green signal
def timecalc(i,j,n1,n2):
    t1 = a + n1/stf[i]  
    t2 = a + n2/stf[j]
    if(t1>t2):
        return t1
    return t2

# time to be assigned
def schedule(t,tmax):
    if(t<tmax):
        return t
    return tmax



file=open("count.txt","r+")  # file where count of each lane is stored
L=file.readlines()  

# reading file and storing data in carcount array and priority queue 
for i in range(0,4):
    x=0
    x+=int(L[i][9])
    x=x*10
    x+=int(L[i][10])        # car count for lane i
    p=Pair(x,i)
    q.insert(p)
    carcount[i]=x

while not q.isEmpty():
    p = q.delete()
    i = p.second            # lane having max no of cars
    # if visit[i]==1 it has been already assigned the time so further assignment could cause starvation
    if(visit[i]==0):
        j= comp[i]          #   complementary lane of i
        n1 = carcount[i]    # carcount of lane i
        n2 = carcount[j]    # carcount of lane j
        visit[i]=1
        visit[j]=1
        t = timecalc(i,j,n1,n2) 
        tassign = schedule(t,tmax)
        print(tassign)   
    


