list_num = [i + 1 for i in range(10)]
print(list_num)

list_even = [i for i in list_num if i % 2 == 0]
print(list_even)

list_odd = [i for i in list_num if not i % 2 == 0]
print(list_odd)