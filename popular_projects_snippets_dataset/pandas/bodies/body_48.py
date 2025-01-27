# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_transform.py
# https://github.com/pandas-dev/pandas/issues/39636
df = DataFrame([], columns=["col1", "col2"])
result = df.transform(lambda x: x + 10)
tm.assert_frame_equal(result, df)

result = df["col1"].transform(lambda x: x + 10)
tm.assert_series_equal(result, df["col1"])
