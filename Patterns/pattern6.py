# Pattern 6
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
# pat61

# Example
# Sample Input

# 5

# Sample Output
# *	*	*		*	*	*	
# *	*				*	*	
# *						*	
# *	*				*	*	
# *	*	*		*	*	*


n = int(input())
nsp = 1;
nst = int((n/2)+1);
#write your code here
for i in range(1,n+1):
    for j in range(1,nst+1):
        print("*\t",end="")
    for j in range(1,nsp+1):
        print("\t",end="");
    for j in range(1,nst+1):
        print("*\t",end="")
    if(i<n/2):
        nst=nst-1;
        nsp=nsp+2;
    else:
        nst=nst+1;
        nsp=nsp-2;
    print();