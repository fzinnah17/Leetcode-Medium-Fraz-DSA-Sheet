#Ques: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Input: x = 2.00000, n = 10
# Output: 1024.00000
class Solution(object):
    def myPow(self, x, n):        
        #1. base cases inside helper function
        #2. create the helper function for both even and odd
        #3. initial condition
        #4. returning the result
        #goal is to break down the problem for even scenarios and odd scenarios
        
        def helper(x, n):
            #base case
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            even_case = helper(x, n//2)
            even_case = even_case * even_case
            
            # this is the odd_case = helper(x, n % 2)
            # odd_case = x * even_case
            
            return x * even_case if n % 2 else even_case #n % 2 means remainder is left
        even_case = helper(x, abs(n)) # make sure to put initial condition when you are done with the recursion condition
        return even_case if n >= 0 else 1 / even_case 
    #return the answer only if the helper has initial condition or more

    # TC: O(n), SC: O(n)
        
        
        
        