'''
Hey Visitor ! This is my code for one of the problems given in my class of ISCP (industry standard coding practice).
Link to the problem : https://www.codechef.com/problems/S10E

'''

import sys
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        mini = sys.maxsize
        happy = 0
        for i in range(n):
            if i < 5:
                if a[i] < mini:
                    happy += 1
                    mini = a[i]
            else:
                mini = min(a[i - 5:i])
                if a[i] < mini:
                    happy += 1
        print(happy)

if __name__ == "__main__":
    main()


'''
------ concept ------

- Import the `sys` module to use the `maxsize` constant.
- Define the `main()` function, the entry point of the program.
- Read the number of test cases `t` from the user.
- Start a loop to iterate through each test case.
- Read the number of elements `n` in the array for the current test case.
- Read a list of space-separated integers from the user, convert them to integers, and store them in the list `a`.
- Initialize the `mini` variable with a large value to find the minimum value within the first 5 elements.
- Initialize the `happy` variable to count the happy elements.
- Iterate through the elements of the array.
- For the first 5 elements, check if the current element is smaller than `mini`, if yes, increment `happy` and update `mini`.
- For elements after the first 5, update `mini` by finding the minimum value within the previous 5 elements, 
    then check if the current element is smaller than `mini` and increment `happy` if true.
- Print the `happy` count for the current test case.
- Repeat the process for all test cases.

'''