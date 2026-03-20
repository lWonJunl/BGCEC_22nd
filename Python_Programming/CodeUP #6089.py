a,r,n=map(int,input().split())
v=a
for i in range(2,n+1):
  v*=r
print(v)