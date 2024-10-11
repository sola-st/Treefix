# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
result = float_frame.apply(lambda x: np.repeat(x.name, len(x)), axis=1)
expected = Series(
    np.repeat(t[0], len(float_frame.columns)) for t in float_frame.itertuples()
)
expected.index = float_frame.index
tm.assert_series_equal(result, expected)
