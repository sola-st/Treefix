# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# GH 24675
cat = Categorical(["A", "B"])
result = cat.set_categories(["A"], rename=True)
expected = Categorical(["A", np.nan])
tm.assert_categorical_equal(result, expected)
