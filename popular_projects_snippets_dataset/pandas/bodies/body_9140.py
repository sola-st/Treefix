# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
# https://github.com/pandas-dev/pandas/issues/23296
cat = Categorical(["a", "b", "c"])
result = cat.take([0, 1, -1], fill_value="a", allow_fill=True)
expected = Categorical(["a", "b", "a"], categories=["a", "b", "c"])
tm.assert_categorical_equal(result, expected)
