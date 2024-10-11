# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
chunksize = 5
N = int(chunksize * 2.5)

# dupe cols
df = tm.makeCustomDataframe(N, 3)
df.columns = ["a", "a", "b"]
with tm.ensure_clean() as path:
    df.to_csv(path, columns=cols, chunksize=chunksize)
    rs_c = read_csv(path, index_col=0)

    # we wrote them in a different order
    # so compare them in that order
    if cols is not None:

        if df.columns.is_unique:
            rs_c.columns = cols
        else:
            indexer, missing = df.columns.get_indexer_non_unique(cols)
            rs_c.columns = df.columns.take(indexer)

        for c in cols:
            obj_df = df[c]
            obj_rs = rs_c[c]
            if isinstance(obj_df, Series):
                tm.assert_series_equal(obj_df, obj_rs)
            else:
                tm.assert_frame_equal(obj_df, obj_rs, check_names=False)

            # wrote in the same order
    else:
        rs_c.columns = df.columns
        tm.assert_frame_equal(df, rs_c, check_names=False)
