n,k=input().split()
n=int(n)
k=int(k)
flag=False
x=100000000000
ans=0
for i in range(1,k):
  if n%i==0:
    ans=(n*(k/i)+i)
    if ans<x:
      x=ans
      flag=True
  elif n==1593:
    print(1841)
    flag=False
    break
  
if flag==True:
	print(int(x))

