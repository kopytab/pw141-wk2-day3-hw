# 1748. Sum of Unique Elements-
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


#look at each number
#track each number and its occurences
#check if the number is already being tracked
#if tracked, increment the count of that number
#if not, track the number


#start a running sum - output
#look through log
#identify unique numbers / by the single count
#if unique, add the number to the running sum

#return output


def sum_unique_numbers(nums):
    output = 0
    hash_map = {}
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num]+=1
    for num, count in hash_map.items():
        if count == 1:
            output += num

    return output

print(sum_unique_numbers([1,2,3,2]), 4)
print(sum_unique_numbers([1,1,1,1,1]), 0)
print(sum_unique_numbers([1,2,3,4,5]), 15)