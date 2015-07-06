def triangles(max):
	L=[1]
	n=0
	while n<max:
		yield L
		if len(L)!=1:
			L=[L[i]+L[i+1] for i in range(0,len(L)-1)]
			L.insert(0,1)
			L.append(1)
			n=n+1
		else:
			L.append(1)
			n=n+1
t=triangles(15)
for i in t:
	print(i) 
