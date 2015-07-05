x=input()
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad perand type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(x))
