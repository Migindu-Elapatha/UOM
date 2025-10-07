m=0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        p=i*j
        if str(p)==str(p)[::-1]and p>m:m=p
print(m)