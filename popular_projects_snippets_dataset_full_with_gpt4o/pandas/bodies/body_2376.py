# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_insert.py
# GH#14291
df = DataFrame()
df.insert(0, "A", ["g", "h", "i"], allow_duplicates=True)
df.insert(0, "A", ["d", "e", "f"], allow_duplicates=True)
df.insert(0, "A", ["a", "b", "c"], allow_duplicates=True)
exp = DataFrame(
    [["a", "d", "g"], ["b", "e", "h"], ["c", "f", "i"]], columns=["A", "A", "A"]
)
tm.assert_frame_equal(df, exp)
