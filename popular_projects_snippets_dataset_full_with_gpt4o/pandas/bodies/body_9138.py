# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
# https://github.com/pandas-dev/pandas/issues/23296
cat = Categorical(["a", "a", "b"])
result = cat.take([0, -1, -1], allow_fill=True)
expected = Categorical(["a", np.nan, np.nan], categories=["a", "b"])
tm.assert_categorical_equal(result, expected)
