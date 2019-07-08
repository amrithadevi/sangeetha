ain,bb=input().split()
ain=int(ain)
bb=int(bb)
s=''
u=2
if(ain+bb<=3):
    for i in range(0,ain+bb):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,ain+bb):
        if(i==u):
            s=s+'0'
            if(u==bb):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif ain==1 and bb==2: 
     print("011")
else:
    print(s)
