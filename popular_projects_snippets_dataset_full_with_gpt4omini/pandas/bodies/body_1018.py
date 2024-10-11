# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py
# GH#38071
labels = {
    "str": list("abcde"),
    "int": range(5),
}[dtype]

mi = MultiIndex.from_arrays([labels] * 2)
df = DataFrame(1.0, index=mi, columns=["A"])

SLC = pd.IndexSlice

expected = df.iloc[iloc, :]
result_get_loc = df.loc[SLC[loc], :]
result_get_locs_level_0 = df.loc[SLC[loc, :], :]
result_get_locs_level_1 = df.loc[SLC[:, loc], :]

tm.assert_frame_equal(result_get_loc, expected)
tm.assert_frame_equal(result_get_locs_level_0, expected)
tm.assert_frame_equal(result_get_locs_level_1, expected)
