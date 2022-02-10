def max_subarray (nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n

        max_sum = max(max_sum, cur_sum)
    return max_sum

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
    max_subarray,
]
tests = [
    ("Test #1", [1,2,3,4], 10),
    ("Test #2", [-1,1,0,-3,3], 3),
    ("Test #3", [-2,1,-3,4,-1,2,1,-5,4], 6),
    ("Test #4", [5,4,-1,7,8], 23),
    ("Test #5", [-2, -3, -1], -1),
    ("Test #6", [1], 1),
    ("Test #7", [-2,1,-3,4,-1,2,1,-5,6], 7),
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
