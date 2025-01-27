# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_function.py
result = data.tolist()
expected = list(data)
tm.assert_equal(result, expected)
