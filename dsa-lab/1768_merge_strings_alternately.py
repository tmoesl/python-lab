"""
Link: https://leetcode.com/problems/merge-strings-alternately/description/

1768 - Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q r s
merged: a p b q r s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c d
word2:    p   q
merged: a p b q c d


Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


# Brute-force: Linear scan
# Time: O(n + m), Space: O(n + m)
class SolutionA:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        limit = min(len(word1), len(word2))

        for i in range(limit):
            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[limit:])
        result.append(word2[limit:])
        return "".join(result)


# Brute-force: Linear scan
# Time: O(n + m), Space: O(n + m)
class SolutionB:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for a, b in zip(word1, word2, strict=False):
            result.append(a + b)

        result.append(word1[len(word2) :])
        result.append(word2[len(word1) :])

        return "".join(result)


if __name__ == "__main__":
    appA = SolutionA()
    appB = SolutionB()

    cases = [["abc", "pqrx"], ["ab", "pqrs"], ["abcd", ""]]

    for word1, word2 in cases:
        print(f"Input: {word1, word2}")
        print(f"SolutionA: {appA.mergeAlternately(word1, word2)}")
        print(f"SolutionB: {appB.mergeAlternately(word1, word2)}\n")
