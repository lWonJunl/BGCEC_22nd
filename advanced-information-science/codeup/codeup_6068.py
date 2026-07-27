#풀이1
n=int(input())
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D') 

#풀이2
a=int(input())
d={9:'A',10:'A',7:'B',8:'B',4:'C',5:'C',6:'C'}
print(d.get(a//10, 'D'))