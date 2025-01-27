# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#5932
# copy on empty with assignment fails
df = DataFrame(index=[0])
df = df.copy()
df["a"] = 0
expected = DataFrame(0, index=[0], columns=["a"])
tm.assert_frame_equal(df, expected)
