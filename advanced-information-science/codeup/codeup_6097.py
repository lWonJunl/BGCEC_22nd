h,w=map(int,input().split()) #가로, 세로 입력력
A=[[0]*w for i in range(h)] #좌표평면 제작
n=int(input()) #막대 개수 입력
for i in range(n): 
  l,d,x,y=map(int,input().split())  #막대 길이, 방향 좌표 입력
  x=x-1
  y=y-1
  if d==0: #막대가 가로일 때
    for m in range(l):
      A[x][y+m]=1
  else: #막대가 세로일 때
    for m in range(l):
      A[x+m][y]=1
for j in range(h):#결과 출력
  for k in range(w):
    print(A[j][k],end=' ')
  print()