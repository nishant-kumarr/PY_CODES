'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/PERMCLEAR

'''


t = int(input("Enter no of testcases : "))

for i in range(t):
    N = int(input("Enter first array size : "))
    A = list(map(int, input("Enter the first array as spaced numbers in one line : ").split()))
    K = int(input("Enter second array size : "))
    B = set(map(int, input("Enter the second array as spaced numbers in one line : ").split()))  
    # Convert B to a set for faster membership testing
    
    # Use a list comprehension to filter A
    arr = [x for x in A if x not in B]
    
    print("Final array is : ",*arr)