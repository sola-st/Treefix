# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
c = Categorical([1, 2, 3], ordered=True)
exp = """[1, 2, 3]
Categories (3, int64): [1 < 2 < 3]"""

assert repr(c) == exp

c = Categorical([1, 2, 3, 1, 2, 3], categories=[1, 2, 3], ordered=True)
exp = """[1, 2, 3, 1, 2, 3]
Categories (3, int64): [1 < 2 < 3]"""

assert repr(c) == exp

c = Categorical([1, 2, 3, 4, 5] * 10, ordered=True)
exp = """[1, 2, 3, 4, 5, ..., 1, 2, 3, 4, 5]
Length: 50
Categories (5, int64): [1 < 2 < 3 < 4 < 5]"""

assert repr(c) == exp

c = Categorical(np.arange(20, dtype=np.int64), ordered=True)
exp = """[0, 1, 2, 3, 4, ..., 15, 16, 17, 18, 19]
Length: 20
Categories (20, int64): [0 < 1 < 2 < 3 ... 16 < 17 < 18 < 19]"""

assert repr(c) == exp
