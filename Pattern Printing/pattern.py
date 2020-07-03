n=int(input())
count=1
for i in range(n):
    print(2*i*'*',end="")
    for j in range(1,n+1-i):
        print(count*10,end="")
        count+=1
    count2=count+2*(((n-i)*(n-i-1))//2)
    for j in range(n-i):
        print((count2+j)*10,end='')
    print("\b")
    print()