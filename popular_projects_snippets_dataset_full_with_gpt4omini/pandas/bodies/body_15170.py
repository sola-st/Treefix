# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
s = Series(Categorical([1, 2, 3]))
exp = """0    1
1    2
2    3
dtype: category
Categories (3, int64): [1, 2, 3]"""

assert repr(s) == exp

s = Series(Categorical(np.arange(10)))
exp = f"""0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: category
Categories (10, {np.int_().dtype}): [0, 1, 2, 3, ..., 6, 7, 8, 9]"""

assert repr(s) == exp
