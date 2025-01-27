# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#44755 reset_index with duplicate column labels
df = multiindex_df.rename_axis("A")
df = df.set_flags(allows_duplicate_labels=flag)

if flag and allow_duplicates:
    result = df.reset_index(allow_duplicates=allow_duplicates)
    levels = [["A", ""], ["A", ""], ["B", "b"]]
    expected = DataFrame(
        [[0, 0, 2], [1, 1, 3]], columns=MultiIndex.from_tuples(levels)
    )
    tm.assert_frame_equal(result, expected)
else:
    if not flag and allow_duplicates:
        msg = (
            "Cannot specify 'allow_duplicates=True' when "
            "'self.flags.allows_duplicate_labels' is False"
        )
    else:
        msg = r"cannot insert \('A', ''\), already exists"
    with pytest.raises(ValueError, match=msg):
        df.reset_index(allow_duplicates=allow_duplicates)
