d=[]
for i in range(11) :
    d.append([])
    for j in range(11) :
        d[i].append(0)
for i in range(10) :
    a = input().split()
    for j in range(10) :
        d[i][j] = int(a[j])
x=1;y=1
d[x][y]=9
while True:
  if d[x][y+1]==0:
    d[x][y+1]=9
    y+=1
  elif d[x][y+1]==2:
    d[x][y+1]=9
    break
  elif d[x][y+1]==1:
     if d[x+1][y]==0:
        d[x+1][y]=9
        x+=1
     elif d[x+1][y]==2:
       d[x+1][y]=9
       break
     else: break   
for j in range(10):  
  for k in range(10):
    print(d[j][k],end=' ')
  print()