# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
vals = ["a", "b", "c"]
arr = pd.array(vals, dtype=dtype)
result = arr.tolist()
expected = vals
tm.assert_equal(result, expected)
