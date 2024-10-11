# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

df1 = tm.makeTimeDataFrame()
df2 = tm.makeTimeDataFrame().rename(columns="{}_2".format)
df2["foo"] = "bar"

with ensure_clean_store(setup_path) as store:

    msg = "keys must be a list/tuple"
    # no tables stored
    with pytest.raises(TypeError, match=msg):
        store.select_as_multiple(None, where=["A>0", "B>0"], selector="df1")

    store.append("df1", df1, data_columns=["A", "B"])
    store.append("df2", df2)

    # exceptions
    with pytest.raises(TypeError, match=msg):
        store.select_as_multiple(None, where=["A>0", "B>0"], selector="df1")

    with pytest.raises(TypeError, match=msg):
        store.select_as_multiple([None], where=["A>0", "B>0"], selector="df1")

    msg = "'No object named df3 in the file'"
    with pytest.raises(KeyError, match=msg):
        store.select_as_multiple(
            ["df1", "df3"], where=["A>0", "B>0"], selector="df1"
        )

    with pytest.raises(KeyError, match=msg):
        store.select_as_multiple(["df3"], where=["A>0", "B>0"], selector="df1")

    with pytest.raises(KeyError, match="'No object named df4 in the file'"):
        store.select_as_multiple(
            ["df1", "df2"], where=["A>0", "B>0"], selector="df4"
        )

    # default select
    result = store.select("df1", ["A>0", "B>0"])
    expected = store.select_as_multiple(
        ["df1"], where=["A>0", "B>0"], selector="df1"
    )
    tm.assert_frame_equal(result, expected)
    expected = store.select_as_multiple("df1", where=["A>0", "B>0"], selector="df1")
    tm.assert_frame_equal(result, expected)

    # multiple
    result = store.select_as_multiple(
        ["df1", "df2"], where=["A>0", "B>0"], selector="df1"
    )
    expected = concat([df1, df2], axis=1)
    expected = expected[(expected.A > 0) & (expected.B > 0)]
    tm.assert_frame_equal(result, expected, check_freq=False)
    # FIXME: 2021-01-20 this is failing with freq None vs 4B on some builds

    # multiple (diff selector)
    result = store.select_as_multiple(
        ["df1", "df2"], where="index>df2.index[4]", selector="df2"
    )
    expected = concat([df1, df2], axis=1)
    expected = expected[5:]
    tm.assert_frame_equal(result, expected)

    # test exception for diff rows
    store.append("df3", tm.makeTimeDataFrame(nper=50))
    msg = "all tables must have exactly the same nrows!"
    with pytest.raises(ValueError, match=msg):
        store.select_as_multiple(
            ["df1", "df3"], where=["A>0", "B>0"], selector="df1"
        )
