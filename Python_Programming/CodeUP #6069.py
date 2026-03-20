#풀이1
a=input()
if a=="A" :
  print('best!!!')
else :
  if a=="B" :
    print('good!!')
  else :
      if a=="C" :
        print('run!')
      else :
         if a=="D" :
            print('slowly~')
         else :
          print('what?')

#풀이2
a={'A':'best!!!','B':'good!!','C':'run!','D':'slowly~'}
print(a.get(input(),"what?"))