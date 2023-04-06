num = int(input())
test_cases = []

for i in range(num):
  start, end = map(int, input().split())
  test_cases.append(end - start)

for distance in test_cases:
  count = 0
  hyper_drive_distance = 1
  distance_left = distance

  while distance_left > 0:
    min_dist = hyper_drive_distance * (hyper_drive_distance + 1) / 2
    max_dist = (hyper_drive_distance + 1) * (hyper_drive_distance + 2) / 2
    
    if count > 0:
      if distance_left >= max_dist:
        hyper_drive_distance += 1
      elif distance_left < min_dist and hyper_drive_distance > 1:
        hyper_drive_distance -= 1

    distance_left -= hyper_drive_distance
    count += 1

  print(count)