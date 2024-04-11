from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for ai, a in enumerate(nums):
        for bi, b in enumerate(nums[ai+1:]):
            bi += ai+1
            if (a+b) == target:
                return [ai, bi]
    return []


# Test cases:
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))
    print(twoSum([9, 11, 12, 35, 22, 44], 66))
    print(twoSum([9, 11, 12, 35, 22, 44], 20))
    print(twoSum([9, 11, 12, 35, 22, 44], 23))
    print(twoSum([9, 0], 9))
