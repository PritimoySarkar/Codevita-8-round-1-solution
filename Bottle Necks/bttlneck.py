from collections import Counter
n=int(input())
l=list(map(int,input().split()))
c=Counter(l)
print(c[c.most_common(1)[0][0]])