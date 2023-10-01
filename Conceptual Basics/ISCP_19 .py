'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/REMOVEBAD

'''

def find_min():
    n = int(input())
    arr = list(map(int,input().split()))
    
    digit_count = {}
    for num in arr:
        if num in digit_count:
            digit_count[num] += 1
        else:
            digit_count[num] = 1

    res =  max(digit_count.values())
    print(n-res)


t = int(input())
for i in range(t):
    find_min()

'''
----- CONCEPT -----
1. Ignoring the explanation for taking input and storing.
2. simply what we are doing is we are taking numbers in an array arr.
3. We are creating a empty dictionary. Then, traverse through array element. if that array is present in 
    dictionary as a key increase its value by 1. if not add a key value pair to dictionary and initialize key to 1.
4. then, find the maximum value. then, subtract with no of elements in array, and print it. as minimum that much 
    no of needed to be removed.
5. That's it.

'''