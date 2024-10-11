# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
length = 2 ** (l_exp + 8) + l_add
s = tm.rands_array(length, 2)

result = hash_array(s, "utf8")
assert not result[0] == result[1]
