class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        maxNum = -101
        pointer = 0
        for num in nums:
            if num > maxNum:
                maxNum = num
                nums[pointer] = num
                pointer += 1

        return pointer


if __name__ == "__main__":
    solutionFinder = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = solutionFinder.removeDuplicates(nums)
    print(nums)
    print(solution)
