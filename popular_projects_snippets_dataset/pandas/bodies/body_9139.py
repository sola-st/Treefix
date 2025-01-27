# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
# -1 was a category
cat = Categorical([-1, 0, 1])
result = cat.take([0, -1, 1], allow_fill=True, fill_value=-1)
expected = Categorical([-1, -1, 0], categories=[-1, 0, 1])
tm.assert_categorical_equal(result, expected)
