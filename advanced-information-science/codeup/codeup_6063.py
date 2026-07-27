#풀이1
a,b=map(int, input().split())
print(int(a if (a>=b) else b))

#풀이2
a,b=map(int, input().split())
print((a>b) and a or b)