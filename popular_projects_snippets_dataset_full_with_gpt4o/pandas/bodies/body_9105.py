# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
c = Categorical([1, 2, np.nan])
c_exp = """[1, 2, NaN]\nCategories (2, int64): [1, 2]"""
assert repr(c) == c_exp

s = Series([1, 2, np.nan], dtype="object").astype("category")
s_exp = """0      1\n1      2\n2    NaN
dtype: category
Categories (2, int64): [1, 2]"""
assert repr(s) == s_exp
