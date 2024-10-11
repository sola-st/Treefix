# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_partial_indexing.py
# GH12685 (partial string with daily resolution or below)
result = df.loc[IndexSlice["2013-03":"2013-03", :], :]
expected = df.iloc[118:180]
tm.assert_frame_equal(result, expected)
