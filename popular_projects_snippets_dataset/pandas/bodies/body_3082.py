# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_duplicated.py
df = DataFrame({"C": [np.nan, 3, 3, None, np.nan], "x": 1}, dtype=object)

result = df.duplicated(keep=keep)
tm.assert_series_equal(result, expected)
