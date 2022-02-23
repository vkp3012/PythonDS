# Pattern 1
# Easy

# 1. You are given a number n.
# 2. You've to create a pattern of * and separated by tab as shown in output format.

# Constraints
# 1 <= n <= 100

# Format
# Input
# A number n

# Output
# pat11

# Example
# Sample Input

# 2

# Sample Output
# *	
# *	*

n = int(input())
#write your code here
nst = 1
for i in range(0,n):
    for j in range(0,nst):
        print("*\t" ,end="");
    nst=nst+1;
    print();