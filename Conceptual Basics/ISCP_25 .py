'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/LEBOMBS

'''

t = int(input("Enter no of test cases : "))

for i in range(t):
    n = int(input("Enter the string length :"))
    s = input("Enter the string : ")

    changes = [0] * n

    for i in range(n):
        if s[i] == '1':
            changes[i] = 1
            if i > 0:
                changes[i - 1] = 1
            if i < n - 1:
                changes[i + 1] = 1

    count = changes.count(0)
    print(count)


'''
----- CONCEPT -----

1. We are taking all the inputs. 
2. then, we will traverse through the string.
3. if '1' is at index 0, we make index 0 and 1 as '1' meaning there by both location is prone to bomb.
4. if '1 is at the (n-1)th index we make (n-1) and (n-1) as '1'.
5. else if location is somewhere in mid we make both previous and next index as '1'.
6. we store all these values in a list equal to size of string - 'n'.
7. then, we count zeroes that is no of room protected and print it. 

'''