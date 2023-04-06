num = int(input())
nums = [0] * num
buildings = list(map(int, input().split()))

def get_watchable_buildings(buildings, num):
  for i in range(num):
    for j in range(num):
      if i != j:
        hide = 0
        a = (buildings[j] - buildings[i]) / (j - i)
        b = buildings[i] - a * i

        for k in range(min(i, j) + 1, max(i, j)):
          if buildings[k] >= a * k + b:
            hide += 1
        
        if hide == 0:
          nums[i] += 1
  
  return max(nums)

max_num = get_watchable_buildings(buildings, num)

print(max_num)