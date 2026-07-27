A=[[0]*19 for i in range(19)] 
n=int(input())
for i in range(n):
  x,y=map(int,input().split())
  A[x-1][y-1]=1
for j in range(19): 
  for k in range(19):
    print(A[j][k],end=' ')
  print()