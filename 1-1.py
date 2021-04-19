nums = [4, 9, 11, 14]
target = 13

def two_sum(nums, target):
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            return [i, i+1]

print(two_sum(nums, target))