# https://bytebytego.com/exercises/coding-patterns/two-pointers/triplet-sum


def find_triplets(nums):
    # Return empty list if input array has less than 3 elements
    if len(nums) < 3:
        return []
    
    # Sort the array to use two-pointer technique
    nums.sort()
    result = []
    
    # Fix the first element and use two pointers for the remaining elements
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

# Test the function
if __name__ == "__main__":
    nums = [0, -1, 2, -3, 1]
    print(find_triplets(nums))  # Output: [[-3, 1, 2], [-1, 0, 1]]