a,b,s=1,2,0
while b<=4000000:
    if b%2==0:s+=b
    a,b=b,a+b
print(s)