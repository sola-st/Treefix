# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 48813
s = Series([1, 2, np.nan])
default_map = defaultdict(lambda: "missing", {1: "a", 2: "b", np.nan: "c"})
expected_default_map = default_map.copy()
s.map(default_map, na_action=na_action)
assert default_map == expected_default_map
