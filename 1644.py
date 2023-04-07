n = int(input())

is_prime = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
  if is_prime[i]:
    primes.append(i)
    for j in range(i * 2, n + 1, i):
      is_prime[j] = False

i, j, count = 0, 0, 0

while j < len(primes):
  summation = sum(primes[i: j + 1])
  
  if summation < n:
    j += 1
  else:
    if summation == n:
      count += 1
    if i < j:
      i += 1
    else:
      j += 1
  
print(count)
