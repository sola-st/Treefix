# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_duplicated.py
df = DataFrame({"A": [0, 1, 1, 2, 0], "B": ["a", "b", "b", "c", "a"]})

result = df.duplicated(keep=keep)
tm.assert_series_equal(result, expected)
