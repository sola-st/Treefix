# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-4679
with tm.ensure_clean(ext) as pth:
    if (c_idx_levels == 1 and c_idx_names) and not (
        r_idx_levels == 3 and not r_idx_names
    ):
        mark = pytest.mark.xfail(
            reason="Column index name cannot be serialized unless "
            "it's a MultiIndex"
        )
        request.node.add_marker(mark)

    # Empty name case current read in as
    # unnamed levels, not Nones.
    check_names = r_idx_names or r_idx_levels <= 1

    df = tm.makeCustomDataframe(
        5, 5, c_idx_names, r_idx_names, c_idx_levels, r_idx_levels
    )
    df.to_excel(pth)

    act = pd.read_excel(
        pth,
        index_col=list(range(r_idx_levels)),
        header=list(range(c_idx_levels)),
    )
    tm.assert_frame_equal(df, act, check_names=check_names)

    df.iloc[0, :] = np.nan
    df.to_excel(pth)

    act = pd.read_excel(
        pth,
        index_col=list(range(r_idx_levels)),
        header=list(range(c_idx_levels)),
    )
    tm.assert_frame_equal(df, act, check_names=check_names)

    df.iloc[-1, :] = np.nan
    df.to_excel(pth)
    act = pd.read_excel(
        pth,
        index_col=list(range(r_idx_levels)),
        header=list(range(c_idx_levels)),
    )
    tm.assert_frame_equal(df, act, check_names=check_names)
