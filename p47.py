aaz,vj=map(int,input().split())
if aaz%10==0:
  aaz=str(aaz)
  c=0
  for i in range(len(aaz)-1,-1,-1):
    if aaz[i]=='0':
      c+=1
  if vj<=c:
    print(aaz)
  else:
    aaz=aaz[:-c]
    aaz=aaz+'0'*vj
    print(aaz)
elif 10%(aaz%10)==0:
  vk=int('1'+'0'*vj)
  while True:
    if vk%aaz==0:
      print(vk)
      break
    else:
      vk+=int('1'+'0'*vj)
else:
  print(str(aaz)+vj*'0')
