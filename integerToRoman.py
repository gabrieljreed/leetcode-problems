"""12 - Integer To Roman."""


class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert integers to roman numerals."""
        rawValues = [
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
        ]
        lookupTable = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        resultString = ""

        minLookupIndex = 0
        while num != 0:
            for i in range(minLookupIndex, len(rawValues)):
                lookupValue = rawValues[i]
                if lookupValue > num:
                    continue
                minLookupIndex = i
                resultString += lookupTable[lookupValue]
                num = num - lookupValue
                break

        return resultString


if __name__ == "__main__":
    solutionFinder = Solution()
    num = 3999
    solution = solutionFinder.intToRoman(num)
    print(solution)
