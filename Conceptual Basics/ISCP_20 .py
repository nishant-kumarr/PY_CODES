'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/PRIMEREVERSE

'''


t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    b = input()
    
    azero = 0
    aone = 0
    bzero = 0
    bone = 0
    
    for i in range(n):
        if(a[i] == '0'):
            azero += 1 
        else:
            aone += 1
        
        if(b[i] == '0'):
            bzero += 1
        else:
            bone += 1
    
    if(azero == bzero and aone == bone):
        print("YES")
    else:
        print("NO")