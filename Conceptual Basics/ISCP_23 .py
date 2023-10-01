'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/TOTR

'''
t=list(map(str,input().split()))
N=int(t[0])

dic={}
dic["_"]=" "
for i in range(26):
    dic[chr(97+i)]=t[1][i]
    dic[chr(97+i).upper()]=t[1][i].upper()
    
    
for i in range(N):
    a=input()
    res=""
    for j in a:
        if j in dic:
            res+=dic[j]
        else:
            res+=j
    print(res)

print(dic)

'''
------ concept ------
1. In first two line we will take the no of sentences to be answered (basically thte no of test cases) and the byteland alphabet 
    equivalence.
2. Then, we create a empty dictionary. and add one key value for _ equals ' '. 
3. Then, we have populated the dictionary for all lower and upper case alphabets.
4. Now, take input and print the corresponding letter using dictionary. 
5. If the letter is not in dictionary print as it is, because as per question only character and space is different. Rest all same.

'''