# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = tm.makeCustomDataframe(nrows, 3)
cols = list(df.columns)
cols[:2] = ["dupe", "dupe"]
cols[-2:] = ["dupe", "dupe"]
ix = list(df.index)
ix[:2] = ["rdupe", "rdupe"]
ix[-2:] = ["rdupe", "rdupe"]
df.index = ix
df.columns = cols
result, expected = self._return_result_expected(df, 1000, dupe_col=True)
tm.assert_frame_equal(result, expected, check_names=False)
