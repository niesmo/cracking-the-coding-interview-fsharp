# Time complexity O(n^2)
# Space complexity O(1)
def two_sum_brute_force (nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if (i == j): continue
            if (nums[i] + nums[j] == target):
                return [i, j]
    return [-1,-1]

# Time complexity O(n)
# Space complexity O(n)
def two_sum_dict (nums, target):
    nums_dict = dict ()
    for i, num in enumerate(nums): nums_dict[num]=i
    for i, num in enumerate(nums):
        remainder = target - num
        match nums_dict[remainder]:
            case None : continue
            case j : return [i, j]

    return [-1, -1] 


from termcolor import colored
# fut => function under test
def validate (description, nums, target, fut):
    [i, j] = fut(nums, target)
    if (i == -1 or j == -1):
        print (colored("[FAIL] ", 'red'), description)
        return

    if (nums[i] + nums[j] == target):
        print (colored("[PASS]", "green"), description)
    else:
        print (colored("[FAIL]", "red"), description)

    return

functions_under_test = [
    two_sum_brute_force,
    two_sum_dict
]
tests = [
    ("Test #1", [2, 7, 11, 15], 9),
    ("Test #2", [2,3,4], 6),
    ("Test #3", [3,4], 7)
]

for fut in functions_under_test:
    for (desc, nums, target) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, nums, target, fut)