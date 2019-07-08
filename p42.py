th,ssh=map(int,input().split())
l=list(map(int,input().split()))
if ssh==1:
    print(min(l))
elif ssh==2:
    print(max(l[0],l[th-1]))
else:
    print(max(l))
