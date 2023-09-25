'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/TWTCLOSE

'''

def sum(arr):
    x = 0
    for i in arr:
        x += i
    print("Total no of tweets open currently : ",x)

N,K = map(int,input("\nEnter no of tweets and clicks as spaced integers : ").split())
arr = [0]*K
for i in range(K):
    x = input("\nEnter the action " + str(i + 1) + " performed: ")
    if(x == 'CLOSEALL'):
        arr = [0]*K
        sum(arr)
    else:
        y = int(x.split()[-1])-1
        if (arr[y] == 0):
            arr[y] = 1
            sum(arr)
        else:
            arr[y] = 0
            sum(arr)
print("\n")
    