# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
df = DataFrame({"a": range(5), "b": ["b1", "b2", "b3", "b4", "b5"]})
# GH 7369, make sure can read a 0-obs dta file
with tm.ensure_clean() as path:
    df.to_stata(path, write_index=False, version=version)
    read_df = read_stata(path)

assert isinstance(read_df.index, pd.RangeIndex)
expected = df.copy()
expected["a"] = expected["a"].astype(np.int32)
tm.assert_frame_equal(read_df, expected, check_index_type=True)
