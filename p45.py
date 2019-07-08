aa1 = int(input())
while aa1%10==0:
    aa1=aa1//10
aa1=str(aa1)
b=aa1[::-1]
if aa1==b:
    print("yes")
else:
    print("no")
