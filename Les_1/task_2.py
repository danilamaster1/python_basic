cube_list = [n ** 3 for n in range(1, 1000, 2)]
result = 0

for idx, val in enumerate(cube_list):
    sum_dig = 0
    while val > 0:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        result += cube_list[idx]
    cube_list[idx] += 17

print(result)
result = 0

for idx, val in enumerate(cube_list):
    sum_dig = 0
    while val > 0:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        result += cube_list[idx]

print(result)