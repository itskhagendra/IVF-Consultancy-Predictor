n=int(input())
for i in range(0,n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    for j in range(0,n)