# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop_duplicates.py
# GH 20516
result = df.drop_duplicates()
tm.assert_frame_equal(result, df)

result = df.copy()
result.drop_duplicates(inplace=True)
tm.assert_frame_equal(result, df)
