# Time complexity O(n^2)
# Space complexity O(1)
def contains_duplicate_brute_fornce (nums):
    if (len(nums) < 2): return True

    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if(nums[i] == nums[j]): return True
    return False

# Time complexity O(n)
# Space complexity O(n)
def contains_duplicate_set (nums):
    nums_set = set (nums)
    return len(nums) > len(nums_set)

from termcolor import colored
# fut => function under test
def validate (description, input, expected, fut):
    # act
    actual = fut(input)

    # assert
    if (expected == actual):
        print (colored("[PASS]", "green"), description)
    else:
        print (colored("[FAIL]", "red"), description)

functions_under_test = [
    contains_duplicate_brute_fornce,
    contains_duplicate_set
]
tests = [
    ("Test #1", [1,2,3,1], True),
    ("Test #2", [1,2,3,4], False),
    ("Test #3", [1,1,1,3,3,4,3,2,4,2], True)
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)