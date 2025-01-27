# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
# GH#16713
df = DataFrame({"A": [1, None], "B": [pd.NaT, pd.to_datetime("2016-01-01")]})
df2 = DataFrame({"A": [2, 3]})
df.update(df2, overwrite=False)
expected = DataFrame(
    {"A": [1.0, 3.0], "B": [pd.NaT, pd.to_datetime("2016-01-01")]}
)
tm.assert_frame_equal(df, expected)
