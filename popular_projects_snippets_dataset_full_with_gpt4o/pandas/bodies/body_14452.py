# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
# GH 2973
with ensure_clean_store(setup_path) as store:

    df = tm.makeTimeDataFrame()

    # test string ==/!=
    df["x"] = "none"
    df.loc[df.index[2:7], "x"] = ""

    store.append("df", df, data_columns=["x"])

    result = store.select("df", "x=none")
    expected = df[df.x == "none"]
    tm.assert_frame_equal(result, expected)

    result = store.select("df", "x!=none")
    expected = df[df.x != "none"]
    tm.assert_frame_equal(result, expected)

    df2 = df.copy()
    df2.loc[df2.x == "", "x"] = np.nan

    store.append("df2", df2, data_columns=["x"])
    result = store.select("df2", "x!=none")
    expected = df2[isna(df2.x)]
    tm.assert_frame_equal(result, expected)

    # int ==/!=
    df["int"] = 1
    df.loc[df.index[2:7], "int"] = 2

    store.append("df3", df, data_columns=["int"])

    result = store.select("df3", "int=2")
    expected = df[df.int == 2]
    tm.assert_frame_equal(result, expected)

    result = store.select("df3", "int!=2")
    expected = df[df.int != 2]
    tm.assert_frame_equal(result, expected)
