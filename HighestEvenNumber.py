def getHighestEvenNumber(number_list):
    highest_even_no = 0
    for number in number_list:
        if number%2 == 0 and number > highest_even_no:
            highest_even_no = number
    return highest_even_no    
        


print(getHighestEvenNumber([81,2,34,4,35,6,7,8,9,50,21,98,65]), end=' is the highest even number in the list. :)')