"""34. Find First and Last Position of Element in sorted array."""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        # Binary search to the number, then expand outwards to find the bounds

        lower = 0
        pivot = len(nums) // 2
        upper = len(nums) - 1

        while True:
            if nums[pivot] == target:
                # Found
                break

            if upper <= lower:
                # Target was not found, return
                return [-1, -1]

            if nums[pivot] > target:
                # Too high, look lower
                upper = pivot
                newPivot = ((upper - lower) // 2) + lower
                if newPivot == pivot:
                    newPivot -= 1
                pivot = newPivot

            elif nums[pivot] < target:
                # Too low, look higher
                lower = pivot
                newPivot = ((upper - lower) // 2) + lower
                if newPivot == pivot:
                    newPivot += 1
                pivot = newPivot

        start = pivot
        end = pivot

        while nums[start] == target:
            start -= 1

        while nums[end] == target:
            end += 1

        return [start, end]


if __name__ == "__main__":
    solutionFinder = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 9
    solution = solutionFinder.searchRange(nums, target)
    print(solution)
