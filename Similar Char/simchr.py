c={chr(i):0 for i in range(97,96+27)}
n=int(input())
s=input()
l=[i for i in s]
count=[]
for i in l:
    c[i]+=1
    count.append(c[i])
q=int(input())
for i in range(q):
    x=int(input())
    print(count[x-1]-1)