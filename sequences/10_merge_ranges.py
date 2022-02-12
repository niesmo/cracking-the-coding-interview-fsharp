from heapq import merge
from unittest.util import sorted_list_difference


class Utilities:
    @staticmethod
    def fst (a):return a[0]

    @staticmethod
    def snd (a):return a[1]

def merge_sort (intervals):
    if(len(intervals) <= 1): return intervals

    intervals.sort(key=Utilities.fst) # nlogn
    merged = []

    for i in range(len(intervals)-1):
        f1, f2 = intervals[i]
        s1, s2 = intervals[i+1]

        if (f2 >= s1): intervals[i+1] = [min(f1, s1), max(f2, s2)]
        else: merged.append(intervals[i])

    merged.append(intervals[-1])
    return merged

from termcolor import colored
# fut => function under test
def validate (description, input, expected, fut):
    # act
    actual = fut(input)

    # assert
    if (expected == actual):
        print (colored("[PASS]", "green"), description)
    else:
        print (colored("[FAIL]", "red"), description, f"Expected: {expected} | Actual: {actual}")

functions_under_test = [
    merge_sort,
]
tests = [
    ("Test #1", [[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ("Test #2", [[1,4],[4,5]], [[1,5]]),
    ("Test #3", [[1,2], [3,4], [4,10], [7,16]], [[1,2], [3,16]]),
    ("Test #4", [[1,5], [17,19], [2,7], [6,18], [7,10]], [[1,19]]),
    ("Test #5", [[1,2], [4,6], [5,10], [5,20]], [[1,2], [4,20]]),
    ("Test #6", [[1,2], [4,10], [5,15], [20,30]], [[1,2], [4,15], [20,30]]),
    ("Test #7", [[1,10], [2, 5]], [[1,10]]),
    ("Test #8", [[1,10], [1, 10], [1,11], [1,9]], [[1,11]]),
    ("Test #9", [[1,10]], [[1,10]]),
    ("Test #10", [], []),
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
