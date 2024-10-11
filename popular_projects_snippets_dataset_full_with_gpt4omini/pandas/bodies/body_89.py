# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series([1, 2, 3], index=["a", "b", "c"])
default_dict = defaultdict(lambda: "blank")
default_dict[1] = "stuff"
result = s.map(default_dict)
expected = Series(["stuff", "blank", "blank"], index=["a", "b", "c"])
tm.assert_series_equal(result, expected)
