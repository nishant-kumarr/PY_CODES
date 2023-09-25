'''

Hey Visitor ! This is my one of basic python program written during very first sem that facilitates below operations on an array : 
1. Take no of test cases.
2. Print array, array element, array sorted in ascending and descending order.

'''


t = int(input())
for i in range(t):
    N = int(input())
    A = []
    for i in range(N):
        A.append(i+1)
    #print the array A
    print(A)              
    #print only the elements from array A
    print(*A)   
    #print the array A sorted in ascending order
    A.sort()
    print(A)            
    #print the array A sorted in descending order
    A.sort(reverse=True)
    print(A) 