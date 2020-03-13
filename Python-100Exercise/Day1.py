
#Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
starting_point = 2000
end_point = 3200
result = ''
while starting_point < end_point:
    if starting_point % 7 == 0 and starting_point % 5 != 0:
        if result is None:
            result = str(starting_point)
        else:
            result += ', ' + str(starting_point)
    starting_point += 1
print(result)
print('END of QUESTION 1')
"""
#Question 2:
#Write a program which can compute the factorial of a given numbers.The results should be printed in a 
#comma-separated sequence on a single line.Suppose the following input is supplied to the program: 
#8 Then, the output should be:40320

"""
numbers = list(input('Please enter number to findout the factorial: '))

for number in numbers:
    factorial = int(number)
    while int(number) > 1:        
        number = int(number) - 1
        factorial *= int(number)
    print(str(factorial) + ',')
print('END of QUESTION 2')    
"""     

#Question 3:
#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
#such that is an integral number between 1 and n (both included). and then the program should print 
#the dictionary.Suppose the following input is supplied to the program: 8

#Then, the output should be:

#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input('Please enter any number: '))
starting_point = 1 
thisdict = {}
while starting_point <= number:
    thisdict[starting_point] = starting_point * starting_point
    starting_point += 1

print(thisdict)
