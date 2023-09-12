"""Longest Common Prefix (#14)."""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Find the longest common prefix of a list of words."""
        # My solution
        result = ""

        if len(strs) == 0:
            return result

        for i in len(strs[0]):
            currentLetter = strs[0][i]

            for string in strs[1:]:
                # Base case: A word is finished, therefore the prefix can't be any longer
                if i >= len(string):
                    return result

                if string[i] != currentLetter:
                    return result

            result += currentLetter
            # TODO: It might not be efficient to append to a string like this, maybe make result an array and
            # convert to a string before returning for performance
        return result

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        """Find the longest common prefix of a list of words."""
        # Cleaner solution from leetcode
        if len(strs) == 0:
            return ""

        firstWord = strs[0]
        for i in len(firstWord):
            for word in strs[1:]:
                if i == len(word) or word[i] != firstWord[i]:
                    return firstWord[:i]

        return firstWord


if __name__ == "__main__":
    solutionFinder = Solution()
    strs = [""]
    solution = solutionFinder.longestCommonPrefix(strs)
    print(solution)
