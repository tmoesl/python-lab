"""
Link: https://leetcode.com/problems/roman-to-integer/description/

13 - Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol:Value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58

Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


# Brute-force: Reverse traversal
# Time: O(n), Space: O(1)
class SolutionA:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev = 0

        for char in reversed(s):
            current = roman[char]

            if current < prev:
                result -= current
            else:
                result += current
            prev = current

        return result


# Brute-force: Traversal with lookahead
# Time: O(n), Space: O(1)
class SolutionB:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        n = len(s)
        result = 0

        for i in range(n):
            current = roman[s[i]]

            if i + 1 < n and current < roman[s[i + 1]]:
                result -= current
            else:
                result += current

        return result


if __name__ == "__main__":
    appA = SolutionA()
    appB = SolutionB()

    cases = ["III", "LVIII", "MCMXCIV"]

    for case in cases:
        print(case)
        print(f"Input: {case} → Integer: {appA.romanToInt(case)}")
        print(f"Input: {case} → Integer: {appB.romanToInt(case)}")
