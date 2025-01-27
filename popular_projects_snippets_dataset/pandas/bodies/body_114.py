# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 39140
with np.errstate(all="ignore"):
    expected = concat([op(string_series) for op in ops], axis=1)
    expected.columns = names
    result = string_series.apply(ops)
    tm.assert_frame_equal(result, expected)
