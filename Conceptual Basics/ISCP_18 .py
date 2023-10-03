'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/CHPINTU

'''

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    
    record = {}
    
    fruit_type = list(map(int,input().split()))
    quantity = list(map(int,input().split()))
    
    i=0
    
    for num in fruit_type:
        if num in record:
            record[num] += quantity[i]
            i += 1
        else:
            record[num] = quantity[i]
            i += 1
            
    res = min(record.values())
    print(res)

'''
----- CONCEPT -----

1. So, what we are doing is firstly, take all the required inputs.
2. Then, create a empty dictionary.
3. Go through the fruit type if that fruits type is available as key in dictionary upadate its value with what we found in 
    basket.
4. if not found in dictionary, create a key value pair with key as fruit type and value as found in basket.
5. In the last, just print the minimum quantity of fruit, to keep chef budget friendly.
6. If it seems, foggy, read question (link above) carefully to make things clear.

'''