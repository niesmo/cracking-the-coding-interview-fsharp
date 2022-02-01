# Time complexity O(N+M)
# Space complexity O(N)
def is_valid_angram_set (str1, str2):
    str1_dict = dict ()
    for s in str1:
        match str1_dict.get(s):
            case None: str1_dict[s] = 1
            case _ : str1_dict[s]+=1
    for s in str2:
        match str1_dict.get(s):
            case None | 0 : return False
            case _ : str1_dict[s] -= 1
    for s in str1_dict:
        if (str1_dict[s] != 0): return False

    return True
        
from termcolor import colored
# fut => function under test
def validate (description, input, expected, fut):
    # act
    str1, str2 = input
    actual = fut(str1, str2)

    # assert
    if (expected == actual):
        print (colored("[PASS]", "green"), description)
    else:
        print (colored("[FAIL]", "red"), description)

functions_under_test = [
    is_valid_angram_set
]
tests = [
    ("Test #1", ["anagram", "nagaram"], True),
    ("Test #2", ["rat", "car"], False),
    ("Test #3", ["aaron", "aron"], False)
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)