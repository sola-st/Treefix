# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#47578
df = DataFrame({"a": [1, 2]})
with tm.assert_produces_warning(None):
    df.loc[:, idxr] = DataFrame({"a": [val, 11]}, index=[1, 2])
expected = DataFrame({"a": [np.nan, val]})
tm.assert_frame_equal(df, expected)
