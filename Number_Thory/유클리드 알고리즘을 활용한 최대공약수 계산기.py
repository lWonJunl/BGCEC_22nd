num1,num2=map(int, input("숫자 2개를 공백을 두고 입력하세요:").split())       #숫자 입력

if num1>=num2:     #num1이 더 큰 경우 
  while True:
    gcd=num2      #처음에 나머지가 0인경우 num2가 gcd
    num1=num1%num2
    if num1!=0:       #나머지가 0이 아닌경우 값 저장, 0이면 break
      gcd=num1
    else:
        break
    num2=num2%num1
    if num2!=0:       #나머지가 0이 아닌 경우 값 저장, 0이면 break
      gcd=num2
    else:
        break
else :      #num2가 더 큰 경우 
  while True:
    gcd=num1      #처음에 나머지가 0인경우 num1가 gcd
    num2=num2%num1
    if num2!=0:       #나머지가 0이 아닌 경우 값 저장, 0이면 break
      gcd=num2
    else:
        break
    num1=num1%num2
    if num1!=0:       #나머지가 0이 아닌 경우 값 저장, 0이면 break
      gcd=num1
    else:
      break

print("gcd =",gcd)      #gcd값 출력
