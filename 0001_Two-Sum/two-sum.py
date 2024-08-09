from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for idx in range(len(nums)):
        difference = target - nums[idx] 

        if difference in hashmap.keys():
            return [hashmap[difference], idx]
        else:
            hashmap[nums[idx]] = idx

if __name__ == "__main__":
    example_nums: list = [2, 7, 11, 15]
    example_target: int = 9
    
    twoSum(nums=example_nums, target=example_target)