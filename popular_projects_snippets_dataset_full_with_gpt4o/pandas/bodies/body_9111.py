# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_repr.py
i = CategoricalIndex(Categorical([1, 2, 3], ordered=True))
exp = """CategoricalIndex([1, 2, 3], categories=[1, 2, 3], ordered=True, dtype='category')"""  # noqa:E501
assert repr(i) == exp

i = CategoricalIndex(Categorical(np.arange(10, dtype=np.int64), ordered=True))
exp = """CategoricalIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], categories=[0, 1, 2, 3, ..., 6, 7, 8, 9], ordered=True, dtype='category')"""  # noqa:E501
assert repr(i) == exp
