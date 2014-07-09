l=[1,3,5,7,4]
def find_element(l,e):
	if e in l:
		return l.index(e)
	else:
		return(-1)
print(find_element(l,3))