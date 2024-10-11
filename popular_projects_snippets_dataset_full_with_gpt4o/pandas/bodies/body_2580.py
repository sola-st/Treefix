# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#12533
df = DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
df[lambda x: "A"] = [11, 12, 13, 14]

exp = DataFrame({"A": [11, 12, 13, 14], "B": [5, 6, 7, 8]})
tm.assert_frame_equal(df, exp)
