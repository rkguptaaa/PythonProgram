some_List = ['a', 'd', 'z','x','e','r','d','s','a','q','r']
#setList = []
#count = 0
#while count < len(some_List):
#    setList.append(some_List[count])
#    if(count+1 < len(some_List) and some_List[count+1] in setList):
#        print(some_List[count+1])
#        some_List.remove(some_List[count+1])
#        setList.remove(some_List[count+1])
#    count += 1
#    
duplicate = []
for item in some_List:
    if(some_List.count(item)>1):
        if item not in duplicate:
            duplicate.append(item) 
        else:
            pass
print(duplicate)