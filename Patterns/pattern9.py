# Pattern 9
# Easy

# 1. You are given a number n.
# 2. You've to create a pattern of * and separated by tab as shown in output format.

# Constraints
# 1 <= n <= 100
#  Also, n is odd.

# Format
# Input
# A number n

# Output
# pat91

# Example
# Sample Input

# 5

# Sample Output
# *				*	
# 	*		*		
# 		*			
# 	*		*		
# *				*

n = int(input())
#write your code here
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print("*\t",end="");
        elif(i+j==n+1):
             print("*\t",end="");
        else:
            print("\t",end="")

    print();