from collections import deque
from enum import Enum

class Symbol(Enum):
    Parens = 0
    SquareBrackets = 1
    CurlyBrackets = 2

def is_valid_parens (s):
    parens_stack = []
    is_valid = True
    def open (c) :
        current = parens_stack[-1][0] if (len(parens_stack) > 0) else None
        match current:
            case None: parens_stack.append((c, 1))
            case l if c == l : parens_stack[-1] = (c, parens_stack[-1][1]+1)
            case l: parens_stack.append((c, 1))

    def close (c):
        nonlocal is_valid
        current = parens_stack[-1][0] if (len(parens_stack) > 0) else None
        match current:
            case None: is_valid = False
            case l if c == l and parens_stack[-1][1] == 1: parens_stack.pop ()
            case l if c == l: parens_stack[-1] = (c, parens_stack[-1][1]-1)
            case l: is_valid = False

    for l in s :
        if not is_valid: return False
        match l :
            case "(": open (Symbol.Parens)
            case ")": close (Symbol.Parens)
            case "[": open (Symbol.SquareBrackets)
            case "]": close (Symbol.SquareBrackets)
            case "{": open (Symbol.CurlyBrackets)
            case "}": close (Symbol.CurlyBrackets)

    return True if (is_valid and len(parens_stack) == 0) else False

def is_valid_parens_clever (text):
    valids = ["()", "[]", "{}"]
    stack = []
    for l in text :
        if (len(stack) > 0 and stack[-1] + l in valids):
            stack.pop ()
        else:
            stack.append(l)

    return True if (len(stack) == 0) else False


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
    is_valid_parens,
    is_valid_parens_clever
]
tests = [
    ("Test #1", "()", True),
    ("Test #2", "()[]{}", True),
    ("Test #3", "([", False),
    ("Test #4", ")", False),
    ("Test #5", "(((())))", True),
    ("Test #6", ")))))", False),
    ("Test #6", "{[}())()]}", False),
    ("Test #7", "{[]}", True)
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
