a,b,c=map(int, input().split())
print(int(a if(a<b and a<c) else b if(b<a and b<c) else c))