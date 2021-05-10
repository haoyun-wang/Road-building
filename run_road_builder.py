
import sys
import math

class city(object):

    def __init__(self,name,x,y,z):
        self.name=name
        self.x=x
        self.y=y
        self.z=z
        self.number=0
    def get_name(self,number):
        if self.number==number:
            return self.name



class graph(object):
    def __init__(self,ver):
        self.ver=ver
        self.graph=[]

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def un(self, parent, rank, x, y):
            x_pre = self.find(parent, x)
            y_pre = self.find(parent, y)


            if rank[x_pre] < rank[y_pre]:
                parent[x_pre] = y_pre
            elif rank[x_pre] > rank[y_pre]:
                parent[y_pre] = x_pre


            else:
                parent[y_pre] = x_pre
                rank[x_pre] += 1

    def MST(self):

        result = []

        a = 0
        b=0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []


        for ver in range(self.ver):
            parent.append(ver)
            rank.append(0)


        while b < self.ver - 1:


            u, v, w = self.graph[a]
            a = a + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                b = b + 1
                result.append([u, v, w])
                self.un(parent, rank, x, y)
        return result
lt=[]
ct=[]
a=0
with open(sys.argv[1]) as config_file:
    for i in config_file:
        try:
            j=i.split(',')
            x=city(j[0],int(j[1].strip()),int(j[2].strip()),int(j[3].strip()))

            ct.append(x)




        except:
          lt.append(i.strip())
ct=sorted(ct,key=lambda item:item.name)
D=int(lt[0])
E=int(lt[1])

for i in ct:
    i.number=a
    a+=1



cs=[]
for i in ct:
    a=ct.index(i)+1
    while a<=len(ct)-1:
        dis=math.sqrt((i.x-ct[a].x)**2+(i.y-ct[a].y)**2+(i.z-ct[a].z)**2)
        ele2=(i.z-ct[a].z)**2
        cost=round(D*dis+E*ele2)
        cs.append([i.number, ct[a].number, cost])
        a += 1

g=graph(len(ct))

for i in cs:

    g.addEdge(int(i[0]),int(i[1]),int(i[2]))

re=g.MST()

for i in re:
   for j in ct:
       if i[0]==j.number:
           i[0]=j.name
for i in re:
   for j in ct:
       if i[1]==j.number:
           i[1]=j.name
print('We should build the following roads:')
am=0
for i in re:
    print(' %s->%s = $%d'%(i[0],i[1],i[2]))
    am+=i[2]
print('For a total cost of $%d.'%am)















