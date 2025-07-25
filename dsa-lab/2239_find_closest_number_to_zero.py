"""
Link: https://leetcode.com/problems/find-closest-number-to-zero/description/

2239 - Find Closest Number to Zero

Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.

Example 1:
Input: nums = [-4,-2,1,4,8]
Output: 1

Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:
Input: nums = [2,-1,1]
Output: 1

Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


Constraints:
1 <= n <= 1000
-105 <= nums[i] <= 105
"""


# Brute-force: Linear scan
# Time: O(n), Space: O(1)
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]  # Alternative: None + initiate

        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(num, closest)
        return closest


if __name__ == "__main__":
    app = Solution()

    cases = [[-4, -2, 11, -1, 1, 8], [2, -4, 3], [4, 5, 0, 2, 3, -1]]

    for case in cases:
        print(f"Input: {case} → Closest to 0: {app.findClosestNumber(case)}")
