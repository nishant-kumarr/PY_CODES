'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/NAME2

'''

def is_subsequence(str1, str2):
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len(str1)

def can_marry(test_cases):
    results = []
    for case in test_cases:
        m, w = case
        if is_subsequence(m, w) or is_subsequence(w, m):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input
T = int(input("Enter no of test cases : "))
test_cases = []
for i in range(T):
    M, W = input("Enter both names separated with space : ").split()
    test_cases.append((M, W))

# Output
results = can_marry(test_cases)
for result in results:
    print(result)

'''
-----  CONCEPT -----

1. Firstly we are reading no of test cases.
2. Then, we iterate a loop and take the names and stores in a list 'test_cases'.
3. then we use function 'can_marry' to check if yes or no and print accordingly.

4. 'can_marry' uses 'is_subsequence' function to check if M is subsequence of W or not and vice versa.
5. and 'can_marry' stores result in results function that what we print in last.
6. what 'is_sequence' does is it iterates through both string character wise and checks if first passed string's character is
    present in second or not. at last we compare and check value of i with first string length to verify if entire string is traversed.
7. Then in the last 'results' list elements are printed.

'''