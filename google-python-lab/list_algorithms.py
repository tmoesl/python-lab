# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.


# Brute-force: linear scan
# Time: O(n), Space: O(n)
def remove_adjacent(nums):
    lst = []
    for item in nums:
        if not lst or lst[-1] != item:
            lst.append(item)
    return lst


# Two-pointer approach
# Time: O(n), Space: O(n)
def remove_adjacent(nums):
    lst = []
    L, R = 0, 1

    while R < len(nums):
        if nums[L] != nums[R]:
            lst.append(nums[L])
        L += 1
        R += 1
    lst.append(nums[-1])
    return lst

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

# Brute-force: combine + sort
# Time: O((n + m) log(n + m)), Space: O(n + m)
def linear_merge(list1, list2):
    combined = list1 + list2
    combined.sort()
    return combined


# Pop from start (inefficient, modifies input lists)
# Time: O(n^2), Space: O(n)
def linear_merge(list1, list2):
    lst = []

    while list1 and list2:
        if list1[0] < list2[0]:
            lst.append(list1.pop(0))  # O(n) per pop(0)
        else:
            lst.append(list2.pop(0))

    lst.extend(list1)
    lst.extend(list2)

    return lst


# Pop from end + reverse (efficient, modifies input lists)
# Time: O(n + m), Space: O(n + m)
def linear_merge(list1, list2):
    lst = []

    while list1 and list2:
        if list1[-1] > list2[-1]:
            lst.append(list1.pop(-1))  # O(1) per pop(-1)
        else:
            lst.append(list2.pop(-1))

    lst.extend(list1)
    lst.extend(list2)
    lst.reverse()  # O(n + m)
    return lst


# Two-pointer merge (efficient, does not modify input lists)
# Time: O(n + m), Space: O(n + m)
def linear_merge(list1, list2):
    lst = []
    L, R = 0, 0
    while L < len(list1) and R < len(list2):
        if list1[L] < list2[R]:
            lst.append(list1[L])
            L += 1
        elif list1[L] > list2[R]:
            lst.append(list2[R])
            R += 1
        else:
            lst.append(list1[L])
            L += 1
            R += 1
    lst.extend(list1[L:])
    lst.extend(list2[R:])

    return lst


if __name__ == "__main__":
    # Example A
    a = [1, 3, 5, 11]
    b = [2, 6, 7, 8, 10, 15]

    lst = linear_merge(a, b)
    print(lst)  # [1, 2, 3, 5, 6, 7, 8, 10, 11, 15]

    # Example B
    a = [1, 5, 5, 7, 11]

    lst = remove_adjacent(a)
    print(lst)  # [1, 3, 5, 11]
