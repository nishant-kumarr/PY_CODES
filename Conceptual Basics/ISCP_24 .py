'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/ANTIPAL

'''
def construct_binary_string(N):
    if N % 2 != 0:
        return -1  # Not possible for odd N
    else:
        # Initialize an empty string
        S = ''

        # Loop through indices from 0 to N-1
        for i in range(N):
            # Alternate between adding '0' and '1' to the string
            if i % 2 == 0:
                S += '0'
            else:
                S += '1'
        
        return S


T = int(input("Enter no of test cases : "))
for i in range(T):
    N = int(input("Enter the string length : "))
    result = construct_binary_string(N)
    
    print(result)
    
'''
----- CONCEPTS -----
1. In question, we have been asked to take T and N as no of test cases and string length.
2. And we have to create a string of length N such that S(i) != T(i), where T(i) = S(N+1-i) for 1<=i<=N, i,e. reverse of string S.
3. There can be many possible strings, we just have to print any one.
4. For that reason what I've done is :
    i) If N is odd, print -1 because we can't create such a string. As in odd length even if we make all the position of the
        string follow the rules there would be a location which will remain same in T and S both. 
        For example : in case of length 9 it would be 5.
    ii) For even length what we are doing is we simply create a string of length N having 0 at even and 1 at odd position. 
5. In this way, we complete this task. Note that many string can be possible we just have to come with anyone.

'''