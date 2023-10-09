"""273 - Integer to English words."""


class Solution:
    def numberToWords(self, num: int) -> str:
        """Convert an integer to English words."""
        resultString = ""

        lut = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }

        suffixes = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion"]

        return resultString


if __name__ == "__main__":
    solutionFinder = Solution()
    num = 123456789
    solution = solutionFinder.numberToWords(num)
    print(solution)
