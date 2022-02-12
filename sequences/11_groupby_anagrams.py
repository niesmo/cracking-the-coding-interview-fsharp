from itertools import groupby
from unittest.util import sorted_list_difference

class utilities:
    @staticmethod
    def fst (v): return v[0]
    @staticmethod
    def snd (v): return v[1]
    @staticmethod
    def word_hash (w):
        acc = 0
        for l in w: acc += ord(l)
        return acc

def groupby_anagrams (strs):
    strs.sort(key=len) # O(nlogn) this is only necessary because the `groupby` call needs list to be sorted
    words_groups = groupby(strs, len) # O(n)
    final_anagrams = []

    for _, strs in words_groups:
        tmp = []
        for w in strs: tmp.append((w, utilities.word_hash(w)))

        tmp.sort(key=utilities.snd)
        tmp = groupby(tmp, utilities.snd)

        for _, anagrams in tmp: final_anagrams.append(list(map(utilities.fst, anagrams)))
    return final_anagrams

def groupby_anagrams_dict (strs):
    anagram_dict = dict ()
    for word in strs:
        sorted_word = "".join(sorted(list(word)))
        match anagram_dict.get(sorted_word):
            case None: anagram_dict[sorted_word] = [word]
            case _ : anagram_dict[sorted_word].append(word)
    return list(anagram_dict.values())


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
    groupby_anagrams,
    groupby_anagrams_dict
]
tests = [
    ("Test #1", ["eat","tea","tan","ate","nat","bat"], [["bat"],["eat","tea","ate"],["tan","nat"]]),
    ("Test #2", [""], [[""]]),
    ("Test #3", ["a"], [["a"]]),
    ("Test #4", ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"], [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]),
]

for fut in functions_under_test:
    for (desc, input, solution) in tests :
        desc = "[" + fut.__name__ + "] " + desc
        validate (desc, input, solution, fut)
