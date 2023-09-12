# Integer to Roman Numeral

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The way to do this by hand is to start with the largest value, and subtract it from the number until you can't anymore. Then move on to the next largest value, and repeat until you reach 0. We'll do the same thing with code.

Example: 58

- 58 - 50 = 8 (L)
- 8 - 5 = 3 (V)
- 3 - 1 = 0 (I)
- 2 - 1 = 0 (I)
- 2 - 1 = 0 (I)
- 58 = "L" + "V" + "I" + "I" + "I" = "LVIII"

## Approach

### Data structures

We define a lookup table (hash map) to quickly convert a given integer value to its roman numeral counterpart.

We also have a list of the "raw values" (i.e. just the integers). This is so that we can save some time by not checking against numbers we've already seen are too big.

> Example: Our starting number is 58. We loop through the first part of the list until we get to 50, add "L" to our result string, and subtract `58 - 50` leaving us with 8. We don't want to loop through values 1000-90 again, since we know our number has to be _equal_ or _smaller_ than the number we just checked.

While we could have used `list(lookupTable.keys())`, and written less code, converting dictionary keys to a list is actually slower, so we sacrifice that for a little bit of speed. In this relatively simple example, I don't think it's too bad, but if we were writing this for something that would scale, it could be better to keep it as one list, so we don't have to worry about two separate variables that need to be kept in sync.

### Loops

Our outer loop will continue until our number to convert reaches 0.

The inner loop is where the magic happens. We start at the `minLookupIndex` - the lowest number we've seen so far (so we aren't checking against 1000 when we've already seen that our number is lower than 100, for example).

Inside the inner loop, we check if the value is greater than our number so far. If it is, we immediately continue to the next iteration of the loop. I like to use the approach of checking the _negative_ conditions first and returning/continuing so we don't get an ever-increasing stack of if statements and indents.

## Complexity

### Time complexity

$$O(1)$$

The number of loop iterations does not increase with the size of the input num because there are a fixed number of Roman numeral characters.

### Space complexity

$$O(k)$$

Where `k` is the number of Roman numeral characters required to represent the output.

The `rawValues` and `lookupTable` variables, are of fixed size, so their space complexity is `O(1)`.

## Code

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert an integer to roman numerals."""
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
```
