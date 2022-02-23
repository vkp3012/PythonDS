# Pattern 8
# Easy

# 1. You are given a number n.
# 2. You've to create a pattern of * and separated by tab as shown in output format.

# Constraints
# 1 <= n <= 100

# Format
# Input
# A number n

# Output
# pat81

# Example
# Sample Input

# 5

# Sample Output
#                 *	
# 			*		
# 		*			
# 	*				
# *

n = int(input())
#write your code here
nsp = n-1;
for i in range(n):
    for j in range(nsp):
        print("\t",end="")
    print("*\t",end="")
    nsp=nsp-1;
    print()