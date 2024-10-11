# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

path = tmp_path / setup_path

# min_itemsize in index with to_hdf (GH 10381)
df = tm.makeMixedDataFrame().set_index("C")
df.to_hdf(path, "ss3", format="table", min_itemsize={"index": 6})
# just make sure there is a longer string:
df2 = df.copy().reset_index().assign(C="longer").set_index("C")
df2.to_hdf(path, "ss3", append=True, format="table")
tm.assert_frame_equal(read_hdf(path, "ss3"), concat([df, df2]))

# same as above, with a Series
df["B"].to_hdf(path, "ss4", format="table", min_itemsize={"index": 6})
df2["B"].to_hdf(path, "ss4", append=True, format="table")
tm.assert_series_equal(read_hdf(path, "ss4"), concat([df["B"], df2["B"]]))
