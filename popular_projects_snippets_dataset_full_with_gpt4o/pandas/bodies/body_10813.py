# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
ct = Categorical(
    ["a", "b", "c", "d"], categories=["a", "b", "c", "d"], ordered=False
)
expected = Categorical(
    [None, "a", "b", "c"], categories=["a", "b", "c", "d"], ordered=False
)
res = ct.shift(1, fill_value=fill_value)
tm.assert_equal(res, expected)
