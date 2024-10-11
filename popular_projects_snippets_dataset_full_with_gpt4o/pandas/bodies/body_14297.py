# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
df1 = tm.makeTimeDataFrame()
df2 = tm.makeTimeDataFrame().rename(columns="{}_2".format)
df2["foo"] = "bar"
df = concat([df1, df2], axis=1)

with ensure_clean_store(setup_path) as store:

    # exceptions
    msg = "append_to_multiple requires a selector that is in passed dict"
    with pytest.raises(ValueError, match=msg):
        store.append_to_multiple(
            {"df1": ["A", "B"], "df2": None}, df, selector="df3"
        )

    with pytest.raises(ValueError, match=msg):
        store.append_to_multiple({"df1": None, "df2": None}, df, selector="df3")

    msg = (
        "append_to_multiple must have a dictionary specified as the way to "
        "split the value"
    )
    with pytest.raises(ValueError, match=msg):
        store.append_to_multiple("df1", df, "df1")

    # regular operation
    store.append_to_multiple({"df1": ["A", "B"], "df2": None}, df, selector="df1")
    result = store.select_as_multiple(
        ["df1", "df2"], where=["A>0", "B>0"], selector="df1"
    )
    expected = df[(df.A > 0) & (df.B > 0)]
    tm.assert_frame_equal(result, expected)
