# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# mixed datetimelike
# GH 7778
expected = DataFrame(
    {
        "A": date_range("20130101", periods=3),
        "B": pd.to_timedelta(np.arange(3), unit="s"),
    }
)
result = expected.apply(lambda x: x, axis=1)
tm.assert_frame_equal(result, expected)
