"""Scratch pad for leetcode problems."""


class Solution:
    """LeetCode Solution class."""
    # TODO: it would be nice to create a snippet for leetcode problems
    # TODO: Make this a git repo

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        string = str(x)
        frontIndex = 0
        backIndex = -1

        while frontIndex < len(string) // 2:
            if string[frontIndex] != string[backIndex]:
                return False

            frontIndex += 1
            backIndex -= 1

        return True


if __name__ == "__main__":
    solutionFinder = Solution()
    solution = solutionFinder.isPalindrome(10)
    print(solution)
