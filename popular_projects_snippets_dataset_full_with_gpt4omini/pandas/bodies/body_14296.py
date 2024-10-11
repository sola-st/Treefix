# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# GH 3577
# append timedelta

df = DataFrame(
    {
        "A": Timestamp("20130101"),
        "B": [
            Timestamp("20130101") + timedelta(days=i, seconds=10) for i in range(10)
        ],
    }
)
df["C"] = df["A"] - df["B"]
df.loc[3:5, "C"] = np.nan

with ensure_clean_store(setup_path) as store:

    # table
    _maybe_remove(store, "df")
    store.append("df", df, data_columns=True)
    result = store.select("df")
    tm.assert_frame_equal(result, df)

    result = store.select("df", where="C<100000")
    tm.assert_frame_equal(result, df)

    result = store.select("df", where="C<pd.Timedelta('-3D')")
    tm.assert_frame_equal(result, df.iloc[3:])

    result = store.select("df", "C<'-3D'")
    tm.assert_frame_equal(result, df.iloc[3:])

    # a bit hacky here as we don't really deal with the NaT properly

    result = store.select("df", "C<'-500000s'")
    result = result.dropna(subset=["C"])
    tm.assert_frame_equal(result, df.iloc[6:])

    result = store.select("df", "C<'-3.5D'")
    result = result.iloc[1:]
    tm.assert_frame_equal(result, df.iloc[4:])

    # fixed
    _maybe_remove(store, "df2")
    store.put("df2", df)
    result = store.select("df2")
    tm.assert_frame_equal(result, df)
