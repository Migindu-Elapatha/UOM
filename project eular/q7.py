primes=[2]
n=3
while len(primes)<10001:
    if all(n%p for p in primes if p*p<=n): primes.append(n)
    n+=2
print(primes[-1])