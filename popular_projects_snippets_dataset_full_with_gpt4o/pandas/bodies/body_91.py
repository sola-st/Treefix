# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 48813
s = Series([1, 2, np.nan])
default_map = defaultdict(lambda: "missing", {1: "a", 2: "b", np.nan: "c"})
result = s.map(default_map, na_action=na_action)
expected = Series({0: "a", 1: "b", 2: "c" if na_action is None else np.nan})
tm.assert_series_equal(result, expected)
