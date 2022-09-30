def fourSum(self, nums, target):
        #JUST BECAUSE IT IS ADDING UP ALL THE NUMBERS TO REACH TARGET IT IS WISE TO SORT THE LIST
        
        #things to look out for:
        #1. Any order
        #2. we have to return 4 numbers and can't stop
        #3. return a list so i!= j, i!= k, i!= l, j!= k, j!= l, k != l distinct
        #4. no duplicates
        #5. two conditions: 1. current index != current index -1 this is base case+ outside
        #6. left != left - 1 this is after incrementing left so this is inside

        #the concept is inside (left pointer) and outside (current index). I will try to use the enumerate method from threeSum problem
        
    nums.sort() #sort the list in ascending order of creation time and space complexity is O(nlogn) where n is the length of the list
    result = [] #list to store the result of the list creation time and space complexity is O(1)
    
    for curr_index, curr_value in enumerate(nums): #enumerate the list creation time and space complexity is O(n) where n is the length of the list
        if curr_index > 0 and curr_value == nums[curr_index - 1]: #skip the duplicate value
            continue
            
        for next_number in range(curr_index + 1, len(nums)): #iterate through the list
            if next_number > curr_index + 1 and nums[next_number] == nums[next_number - 1]:
                continue 
                    
            left = next_number + 1 
            right = len(nums) - 1
                    
            while left < right: #while the left pointer is less than the right pointer
                totalFoursum = curr_value + nums[next_number]+nums[left] + nums[right] #calculate the total of the four sum values for the list
                if totalFoursum > target: #if the total is greater than the target value then decrement the right pointer by 1
                    right -=1
                        
                elif totalFoursum < target:     #if the total is less than the target value then increment the left pointer by 1
                    left += 1
                            
                else:   #if the total is equal to the target value then append the result of the list and increment the left pointer by 1 and decrement the right pointer by 1
                    result.append([curr_value, nums[next_number],nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left -1]: #skip the duplicate value for left pointer this time and increment the left pointer by 1
                        left += 1
    return result