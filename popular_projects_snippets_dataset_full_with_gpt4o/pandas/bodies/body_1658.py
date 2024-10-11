# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
left, right = left_right

out = merge(left, right, how="outer")
assert len(out) == len(left)
tm.assert_series_equal(out["left"], -out["right"], check_names=False)
result = out.iloc[:, :-2].sum(axis=1)
tm.assert_series_equal(out["left"], result, check_names=False)
assert result.name is None
