# 풀이1
n=int(input())
if n//3==1 :
  print("spring")
else:
  if n//3==2:
    print("summer")
  else:
    if n//3==3:
      print("fall")
    else:
      print("winter")

# 풀이2
a=int(input())
d={1:'spring',2:'summer',3:'fall'}
print(d.get(a//3, 'winter'))

# 풀이3
month = int(input())
season = {0:'winter',1:'spring',2:'summer',3:'fall'}
month = (month//3)%4
print(season[month])