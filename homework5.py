immutable_var = 1, 2, 3, True, 'apple'
print(immutable_var)
print(type(immutable_var))
immutable_var[0] = 200
print(immutable_var) #консоль выдаёт ошибку т.к immutable_var тип 'tuple' т.е неизменяем
mutable_list = ([1, 2], 'a', 'b')
mutable_list[0][0] = 2
print(mutable_list)