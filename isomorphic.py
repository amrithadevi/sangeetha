try:
	s1=str(raw_input())
	s2=str(raw_input())
	a=[]
	b=[]
	d=[]
	c=0
	n=len(s1)
	for i in range(0,n):
		if s1[i] in a :
			b.append(i)
		else:
			a.append(s1[i])
	for i in range(0,n):
		if(s1[i]==s1[c]):
			d.append(i)
		else: 
			pass
	x=len(d)-1
	while(x!=0):
		i=d[x]
		j=d[x-1]
		if (s2[i]==s2[j]):
			print "true"
		else:
			print "false"
		x=x-1
except:
	print "Invalid"
