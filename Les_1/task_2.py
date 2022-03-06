"""2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Решить задачу под пунктом b, не создавая новый список."""

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

