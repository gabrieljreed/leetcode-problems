"""34. Find First and Last Position of Element in sorted array."""


class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        lower = 0
        pivot = len(nums) // 2
        upper = len(nums) - 1

        while lower <= upper:
            pivot = ((upper - lower) // 2) + lower

            if nums[pivot] == target:
                # Found
                return pivot

            elif nums[pivot] > target:
                # Too high, look lower
                upper = pivot - 1

            elif nums[pivot] < target:
                # Too low, look higher
                lower = pivot + 1

        return -1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        # Binary search to the number, then expand outwards to find the bounds
        pivot = self.binarySearch(nums, target)

        if pivot == -1:
            return [-1, -1]

        start = pivot
        end = pivot

        for i in range(pivot, 0, -1):
            if nums[i - 1] != target:
                break
            start = i - 1

        for i in range(pivot, len(nums)):
            if nums[i] != target:
                break
            end = i

        return [start, end]


if __name__ == "__main__":
    solutionFinder = Solution()
    nums = [5,7,7,8,8,10]
    target = 10
    solution = solutionFinder.searchRange(nums, target)
    print(solution)
