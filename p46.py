vvj=int(input())
vvk=list(map(int,input().split()))
az=0
by=0
vvk.sort(reverse=True)
for i in vvk:
  vvk=az+i
  if by>vvk:
    az=vvk
  else:
    az=by
    by=vvk
print(az,by)
