"""
Solve: https://neetcode.io/problems/duplicate-integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

from collections import defaultdict


def has_duplicate(*, nums: list[int]) -> bool:
    tracker: dict[int, int] = defaultdict(int)
    for num in nums:
        if num in tracker:
            return True
        tracker[num] += 1
    return False
