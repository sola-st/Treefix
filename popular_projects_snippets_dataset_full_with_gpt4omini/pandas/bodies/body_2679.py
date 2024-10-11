# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# https://github.com/pandas-dev/pandas/issues/32992
df = DataFrame([[1, nulls_fixture], [2, "a"]], dtype=object)
result = df.drop_duplicates()
tm.assert_frame_equal(result, df)
