min_num, max_num = map(int, input().split())

n = int(max_num ** 0.5)

is_prime = [True] * (n + 1)
primes = []

for i in range(2, n + 1):
  if is_prime[i]:
    primes.append(i)
    for j in range(2 * i, n + 1, i):
      is_prime[j] = False

is_true = [True] * (max_num - min_num + 1)
count = max_num - min_num + 1

for i in primes:
  start = min_num - min_num % (i ** 2) + i ** 2
  if min_num % (i ** 2) == 0:
    start = min_num
  for j in range(start, max_num + 1, i ** 2):
    if is_true[j - min_num] == True:
      is_true[j - min_num] = False
      count -= 1

print(count)
