def twoSum(nums, target): 
	# YOUR ANSWER
	solution = {} 
	
      	for i in range(len(nums)):
		temp = target - nums[i]
        	if temp in solution:
			return [solution[temp],i]
		else:
			 solution[nums[i]]=i
		# Does not work for all the cases, weird
		"""for j in range(i, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]"""
nums =[3,2,4]
target = 6
answer = twoSum(nums, target)
print(answer)
