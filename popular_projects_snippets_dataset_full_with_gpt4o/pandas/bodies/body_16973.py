# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH 18447

first = Series([], dtype="M8[ns]").dt.tz_localize(tz)
dtype = None if values else np.float64
second = Series(values, dtype=dtype)

expected = DataFrame(
    {
        0: Series([pd.NaT] * len(values), dtype="M8[ns]").dt.tz_localize(tz),
        1: values,
    }
)
result = concat([first, second], axis=1)
tm.assert_frame_equal(result, expected)
