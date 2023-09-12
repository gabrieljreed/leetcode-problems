"""#27"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        for i, num in enumerate(nums):
            if num == val:
                continue
            if i != pointer:
                nums[pointer] = num
            pointer += 1

        return pointer


if __name__ == "__main__":
    solutionFinder = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = solutionFinder.removeElement(nums, val)
    print(nums)
    print(solution)
