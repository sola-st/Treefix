# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
s = pd.Series([True, False, True])
result = s.replace({"asdf": "asdb", True: "yes"})
expected = pd.Series(["yes", False, "yes"])
tm.assert_series_equal(result, expected)
