d=[]
for i in range(19) :
    d.append([])
    for j in range(19) :
        d[i].append(0)
for i in range(19) :
    a = input().split()
    for j in range(19) :
        d[i][j] = int(a[j])
n = int(input())
for i in range(n) :
    x,y=map(int,input().split())
    for j in range(19) :
        if d[j][y-1]==0 :
            d[j][y-1]=1
        else :
            d[j][y-1]=0
        if d[x-1][j]==0 :
            d[x-1][j]=1
        else : d[x-1][j]=0
for j in range(19):
  for k in range(19):
    print(d[j][k],end=' ')
  print()