# Time complexity O(n^2)
# Space complexity O(1)
def maximum_profit_brute_force (prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if (profit > max_profit):
                max_profit = profit

    return max_profit

# Time complexity O()
# Space complexity O()
def maximum_profit_min_max (prices):
    def index_of_min (nums, start=0):
        min, min_idx = [nums[start], start]
        for i, x in enumerate(nums[start:], start):
            if (x < min): 
                min = x 
                min_idx = i
        return min_idx
    def index_of_max(nums, start=0):
        max, max_idx = [nums[start], start]
        for i, x in enumerate(nums[start:], start):
            if (x > max): 
                max = x 
                max_idx = i
        return max_idx

    if (len(prices)<2): return 0
    min_idx = index_of_min (prices)
    max_idx_after_min = index_of_max(prices, min_idx)
    if (min_idx < max_idx_after_min):
        return prices[max_idx_after_min] - prices[min_idx]

    return 0

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
    maximum_profit_brute_force,
    maximum_profit_min_max
]
tests = [
    ("Test #1", [7,1,5,3,6,4], 5),
    ("Test #2", [7,6,4,3,1], 0)
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)