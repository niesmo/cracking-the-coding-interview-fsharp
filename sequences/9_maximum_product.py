def max_product_brute_force (nums):
    max_product = nums[0] * nums[1] * nums[2]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range (j+1, len(nums)):
                max_product = max(max_product, nums[i]*nums[j]*nums[k])

    return max_product

def max_product_sort (nums):
    nums.sort (reverse=True) # assuming this is nlogn
    return max(nums[0] * nums[1] * nums[2] , nums[-1] * nums[-2] * nums[0])

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
    max_product_brute_force,
    max_product_sort,
]
tests = [
    ("Test #1", [1,2,3], 6),
    ("Test #2", [1,2,3,4], 24),
    ("Test #3", [-1,-2,-3], -6),
    ("Test #4", [-100,-98,-1,2,3,4], 39200)
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
