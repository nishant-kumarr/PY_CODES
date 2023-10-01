'''
Hey visitor ! This is my code that facilitates the solution to below requirement.

Que : Write a program that accepts a hash-separated sequence of words as input and prints 
    the words in a hash-separated sequence after sorting them alphabetically in reverse order.

Input:
hey#input#bye

Output:
input#hey#bye

'''

input_string = input("Enter the string : ")

words = input_string.split('#')

words.sort(reverse=True)

output_string = '#'.join(words)

print(output_string,end ='')