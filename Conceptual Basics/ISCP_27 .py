'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/SALARY

'''

t = int(input())

for i in range(t) : 
    n = int(input())
    arr = list(map(int,input().split()))
    
    minPaid = min(arr)
    
    count = 0
    for j in arr:
        count += (j-minPaid)
        
    print(count)