# square by using lamda expression
my_list = [5,3,4]

print(list(map(lambda item : item ** 2, my_list )))

# sorting in tuple

a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key = lambda k : k[1])

print(a)