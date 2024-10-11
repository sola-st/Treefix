# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 25196 37544
data = DataFrame([[1, 2], [3, 4]], columns=["c0", "c1"], index=["i0", "i1"])

result = data.apply(dict, axis=0)
expected = Series([{"i0": 1, "i1": 3}, {"i0": 2, "i1": 4}], index=data.columns)
tm.assert_series_equal(result, expected)

result = data.apply(dict, axis=1)
expected = Series([{"c0": 1, "c1": 2}, {"c0": 3, "c1": 4}], index=data.index)
tm.assert_series_equal(result, expected)
