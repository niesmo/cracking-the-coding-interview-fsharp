def max_subarray_product_brute_force (nums):
    curr_product = 1
    max_product = nums[0]

    for i in range(len(nums)):
        curr_product = 1
        for j in range(i, len(nums)):
            curr_product *= nums[j]
            max_product = max(max_product, curr_product)

    return max_product

def max_subarray_product (nums):
    max_product = nums[0]
    cur_product_max = nums[0]
    cur_product_min = nums[0]

    for n in nums[1:]:
        if n < 0:
            cur_product_min, cur_product_max = cur_product_max, cur_product_min    

        cur_product_min = min(n, cur_product_min * n)
        cur_product_max = max(n, cur_product_max * n)

        max_product = max(max_product, cur_product_max)

    return max_product

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
    max_subarray_product_brute_force,
    max_subarray_product,
]
tests = [
    ("Test #1", [2,3,-2,4], 6),
    ("Test #2", [-2,0,-1], 0),
    ("Test #3", [-2,1,-3,4,-1,2,1,-5,4], 960),
    ("Test #4", [-2,1,-3,4,0,2,1,-5,4,-2], 80),
    ("Test #5", [3,-1,4], 4),
    ("Test #6", [2,-5,-2,-4,3], 24),
    ("Test #7", [2,-5,-2,3,-4,3], 72),
    ("Test #8", [-6, 4, -5, 8, -10, 0, 8], 1600),
    ("Test #9", [40, 0, -20, -10], 200),
    ("Test #10", [2,3,-2,4,  0  ,2,-5,-2,-4,3,  0  ,3,-1,4], 24),
    
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
