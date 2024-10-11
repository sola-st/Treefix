# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#38831
df = DataFrame(columns=["A", "B"])
other = DataFrame({"B": [1, 2]})
df[indexer] = other
expected = DataFrame({"A": [np.nan] * 2, "B": [1, 2]})
expected["A"] = expected["A"].astype("object")
tm.assert_frame_equal(df, expected)
