nn1 = int(input())
a1 = list(map(int,input().split()))
c,l = 0,[]
b = [x for x in range(1,nn1+1)]
for i in a1:
  if i in b:
    b.remove(i)
d = 0
for i in range(0,nn1-1):
  p = a1[i]
  for j in range(i+1,nn1):
    if p == a1[j]:
      if p < b[d]:
        a1[j] = b[d]
        c += 1
      else:
        a1[i] = b[d]
        c += 1
      d += 1
print(c)
print(*a1)
