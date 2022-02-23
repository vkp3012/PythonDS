# Pattern 3
# Easy

# 1. You are given a number n. 2. You've to create a pattern of * and separated by tab as shown in output format.


# Constraints
# 1 <= n <= 10

# Format
# Input
# A number n

# Output
# pat31

# Example
# Sample Input

# 5

# Sample Output
#               *	
# 			*	*	
# 		*	*	*	
# 	*	*	*	*	
# *	*	*	*	*

n = int(input())
nst = 1;
nsp = n-1;
#write your code here
for i in range(0,n):
    for j in range(0,nsp):
        print("\t",end="");
    
    for j in range(0,nst):
        print("*\t",end="");
    
    nsp = nsp-1;
    nst = nst+1;
    print();