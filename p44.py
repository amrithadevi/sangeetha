Nn1,P1,Q1,R1=input().split()
lists=list(map(int,input().split()))
Nn1=int(Nn1)
P1=int(P1)
Q1=int(Q1)
R1=int(R1)
c1=[]
for i in range(0,len(lists)):
    for j in range(i,len(lists)):
        for k in range(j,len(lists)):
            c1.append(P1*lists[i]+Q1*lists[j]+R1*lists[k])
print(max(c1))
