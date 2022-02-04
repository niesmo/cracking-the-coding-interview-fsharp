from turtle import back


def product_of_array_except_self_brute_force (nums):
    result = []
    l = len(nums)
    for i in range(l):
        product = 1
        for j in range(l):
            if (i == j): continue
            product *= nums[j] 
        result.append(product)
    return result

def product_of_array_except_self_linear (nums):
    forward = [nums[0]]
    backward = [x for x in nums]

    for i in range(1, len(nums)): forward.append (forward[i-1] * nums[i])
    for i in range(len(nums)-2, -1, -1): backward[i] = backward[i+1] * nums[i]

    # nums     = [ 2   3  4  5 ]
    # forward  = [ 2   6  24 120]
    # backward = [ 120 60 20 5]
    # res      = [ 60  40 30 24]

    res = [backward[1]]
    for i in range (1, len(nums)):
        if (i == len(nums) - 1): res.append(forward[i-1])
        else: res.append(forward[i-1] * backward[i+1])

    return res

def product_of_array_except_self_constant (nums):
    return nums

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
    product_of_array_except_self_brute_force,
    product_of_array_except_self_linear,
    product_of_array_except_self_constant
]
tests = [
    ("Test #1", [1,2,3,4], [24,12,8,6]),
    ("Test #2", [-1,1,0,-3,3], [0,0,9,0,0]),
    ("Test #3", [4,3,2,1,2], [12,16,24,48,24]),
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
