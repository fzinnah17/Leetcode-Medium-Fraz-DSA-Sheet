def threeSum(self, nums):
    result = [] # list to store the result
    nums.sort() # sort the list in ascending order
    
    for curr_index, curr_value in enumerate(nums): # enumerate the list
        if curr_index > 0 and curr_value == nums[curr_index - 1]: # skip the duplicate value
            continue # continue to the next iteration
            
        left, right = curr_index + 1, len(nums)-1 # set the left and right pointer
        
        while left < right: # while the left pointer is less than the right pointer
            total = curr_value + nums[left] + nums[right] # calculate the total
            if total > 0:   # if the total is greater than 0
                right -= 1 # move the right pointer to the left/decrement the right pointer
                
            elif total < 0: # if the total is less than 0 
                left += 1   # move the left pointer to the right/increment the left pointer
            
            else: # if the total is equal to 0
                result.append([curr_value, nums[left], nums[right]]) # append the result
                left += 1  # move the left pointer to the right/increment the left pointer
                while left < right and nums[left] == nums[left - 1]:    # skip the duplicate value for left pointer this time
                    left += 1  # move the left pointer to the right/increment the left pointer
    return result # return the result of the list 