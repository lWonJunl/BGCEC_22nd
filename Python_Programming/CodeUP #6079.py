a=int(input())
d=0
for i in range(1,a+1):
  d+=i
  if d>=a:
    print(i)
    break