# Pattern 5
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
# pat51

# Example
# Sample Input

# 5

# Sample Output
#       *	
# 	*	*	*	
# *	*	*	*	*	
# 	*	*	*	
# 		*

n = int(input())
#write your code here
nsp = int(n/2);
nst = 1;
for i in range(1,n+1):

    for j in range(1,nsp+1):
        print("\t",end="");

    for j in range(1,nst+1):
        print("*\t",end="");
    
    if(i<=n/2):
        nsp=nsp-1;
        nst=nst+2;
    else:
        nsp=nsp+1;
        nst=nst-2;
    
    print()