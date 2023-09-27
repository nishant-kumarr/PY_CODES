'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/ATTIC

'''

t = int(input("Enter no of test cases : "))

for i in range(t):
    s = input("Enter the string : ")
    
    i = 0
    count = 0
    temp = 0
    arrindex = 0
    arr = ['0']*len(s)
    while i < len(s):       # Traversing the string
        if(s[i] == '.'):        
            temp += 1                       # temp to count how many of '.' are together.
            arr[arrindex] = temp + 1        # In the string if '.' found storing it in a list.
        elif(s[i] == '#'):
            temp = 0
            arrindex += 1                   # if '#' encountered simply putting zero 
        i += 1
            
    axx = 0
    count = 0
    for i in arr:               #checking in list how many days will be required 
        if(int(i) > axx):       # if they prepared of smaller jump and bigger jump encounter no of days increases
            axx = i
            count += 1
    print("They will take",count,"days")