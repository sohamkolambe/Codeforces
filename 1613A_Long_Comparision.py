testcases=int(input())

while testcases!=0:
	x1,p1=input().split()
	x2,p2=input().split()
	x1=int(x1)
	x2=int(x2)
	p1=int(p1)
	p2=int(p2)

	minm=min(p1,p2)

	p1=p1-minm
	p2=p2-minm
	
	if p1 >=7:
		print(">")
	elif p2 >+7:
		print("<")
	else:
		for i in range(0,p1):
			x1 *=10
		for i in range(0,p2):
			x2*=10
		if x1<x2:
			print("<")
		elif x1>x2:
			print(">")
		else:
			print("=")
    
    
	testcases-=1

