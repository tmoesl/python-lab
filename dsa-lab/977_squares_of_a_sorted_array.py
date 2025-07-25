"""
Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

977 - Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


# Brute-force: Linear scan and sort
# Time: O(n log n), Space: O(n)
class SolutionA:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [num**2 for num in nums]
        result.sort()

        return result


# Two-pointer
# Time: O(n), Space: O(n)
# Alternative: Instead of reverse, initiate list with 0s and fill from the end using a backward index.
class SolutionB:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        L, R = 0, len(nums) - 1

        while L <= R:
            if abs(nums[L]) < abs(nums[R]):
                result.append(nums[R] ** 2)
                R -= 1
            else:
                result.append(nums[L] ** 2)
                L += 1

        result.reverse()
        return result


if __name__ == "__main__":
    appA = SolutionA()
    appB = SolutionB()

    cases = [[-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11]]

    for case in cases:
        print(f"Input: {case}")
        print(f"SolutionA: {appA.sortedSquares(case)}")
        print(f"SolutionB: {appB.sortedSquares(case)}\n")
