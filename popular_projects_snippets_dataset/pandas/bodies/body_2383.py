# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_coercion.py
# .at case fixed by GH#45121 (best guess)
df = DataFrame(index=["A", "B", "C"])
df["D"] = 0

indexer_al(df)["C", "D"] = 2
expected = DataFrame({"D": [0, 0, 2]}, index=["A", "B", "C"], dtype=np.int64)
tm.assert_frame_equal(df, expected)

indexer_al(df)["C", "D"] = 44.5
expected = DataFrame({"D": [0, 0, 44.5]}, index=["A", "B", "C"], dtype=np.float64)
tm.assert_frame_equal(df, expected)

indexer_al(df)["C", "D"] = "hello"
expected = DataFrame({"D": [0, 0, "hello"]}, index=["A", "B", "C"], dtype=object)
tm.assert_frame_equal(df, expected)
