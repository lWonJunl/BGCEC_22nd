a,d,c=map(int,input().split())
f=0
for r in range (0,a):
  for g in range (0,d):
    for b in range (0,c):
      print(r,g,b)
      f+=1
print(f)