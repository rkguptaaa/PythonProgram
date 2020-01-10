my_dict = {num : num * 2 for num  in [1,2,3] }

print(my_dict)

#find duplicate in the list

some_List = ['a', 'd', 'z','x','e','r','d','s','a','q','r']


duplicate = list(set([num for num in some_List if some_List.count(num) > 1]))

print(duplicate)

print(set(some_List))