from math import pow, floor

s_now, N, K, r1, r2, c1, c2 = map(int, input().split())

board = [[0] * int(c2 - c1 + 1) for i in range(r1, r2 + 1)]

def fractal(s, r, c):
  min_num = int((N - K) * pow(N, s - 1) / 2)
  max_num = int((N + K) * pow(N, s - 1) / 2) 

  for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
      if i >= r + min_num and i < r + max_num and j >= c + min_num and j < c + max_num:
        board[i - r1][j - c1] = 1

  if s > 1:
    if s == s_now:
      for i in range(floor(r1 / pow(N, s - 1)), floor(r2 / pow(N, s - 1)) + 1):
        for j in range(floor(c1 / pow(N, s - 1)), floor(c2 / pow(N, s - 1)) + 1):
          fractal(s - 1, int(r + i * int(pow(N, s - 1))), int(c + j * int(pow(N, s - 1))))
    else:
      for i in range(N):
        for j in range(N):
          fractal(s - 1, int(r + i * int(pow(N, s - 1))), int(c + j * int(pow(N, s - 1))))

fractal(s_now, 0, 0)

for row in board:
   print(''.join(str(x) for x in row))
