# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

frame = float_frame
old_index = frame.index
arrays = np.arange(len(old_index) * 2, dtype=np.int64).reshape(2, -1)
new_index = MultiIndex.from_arrays(arrays, names=["first", "second"])
frame.index = new_index

with tm.ensure_clean("__tmp_to_csv_multiindex__") as path:

    frame.to_csv(path, header=False)
    frame.to_csv(path, columns=["A", "B"])

    # round trip
    frame.to_csv(path)

    df = self.read_csv(path, index_col=[0, 1], parse_dates=False)

    # TODO to_csv drops column name
    tm.assert_frame_equal(frame, df, check_names=False)
    assert frame.index.names == df.index.names

    # needed if setUp becomes a class method
    float_frame.index = old_index

    # try multiindex with dates
    tsframe = datetime_frame
    old_index = tsframe.index
    new_index = [old_index, np.arange(len(old_index), dtype=np.int64)]
    tsframe.index = MultiIndex.from_arrays(new_index)

    tsframe.to_csv(path, index_label=["time", "foo"])
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        recons = self.read_csv(path, index_col=[0, 1], parse_dates=True)

    # TODO to_csv drops column name
    tm.assert_frame_equal(tsframe, recons, check_names=False)

    # do not load index
    tsframe.to_csv(path)
    recons = self.read_csv(path, index_col=None)
    assert len(recons.columns) == len(tsframe.columns) + 2

    # no index
    tsframe.to_csv(path, index=False)
    recons = self.read_csv(path, index_col=None)
    tm.assert_almost_equal(recons.values, datetime_frame.values)

    # needed if setUp becomes class method
    datetime_frame.index = old_index

with tm.ensure_clean("__tmp_to_csv_multiindex__") as path:
    # GH3571, GH1651, GH3141

    def _make_frame(names=None):
        if names is True:
            names = ["first", "second"]
        exit(DataFrame(
            np.random.randint(0, 10, size=(3, 3)),
            columns=MultiIndex.from_tuples(
                [("bah", "foo"), ("bah", "bar"), ("ban", "baz")], names=names
            ),
            dtype="int64",
        ))

    # column & index are multi-index
    df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=2, c_idx_nlevels=4)
    df.to_csv(path)
    result = read_csv(path, header=[0, 1, 2, 3], index_col=[0, 1])
    tm.assert_frame_equal(df, result)

    # column is mi
    df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=1, c_idx_nlevels=4)
    df.to_csv(path)
    result = read_csv(path, header=[0, 1, 2, 3], index_col=0)
    tm.assert_frame_equal(df, result)

    # dup column names?
    df = tm.makeCustomDataframe(5, 3, r_idx_nlevels=3, c_idx_nlevels=4)
    df.to_csv(path)
    result = read_csv(path, header=[0, 1, 2, 3], index_col=[0, 1, 2])
    tm.assert_frame_equal(df, result)

    # writing with no index
    df = _make_frame()
    df.to_csv(path, index=False)
    result = read_csv(path, header=[0, 1])
    tm.assert_frame_equal(df, result)

    # we lose the names here
    df = _make_frame(True)
    df.to_csv(path, index=False)
    result = read_csv(path, header=[0, 1])
    assert com.all_none(*result.columns.names)
    result.columns.names = df.columns.names
    tm.assert_frame_equal(df, result)

    # whatsnew example
    df = _make_frame()
    df.to_csv(path)
    result = read_csv(path, header=[0, 1], index_col=[0])
    tm.assert_frame_equal(df, result)

    df = _make_frame(True)
    df.to_csv(path)
    result = read_csv(path, header=[0, 1], index_col=[0])
    tm.assert_frame_equal(df, result)

    # invalid options
    df = _make_frame(True)
    df.to_csv(path)

    for i in [6, 7]:
        msg = f"len of {i}, but only 5 lines in file"
        with pytest.raises(ParserError, match=msg):
            read_csv(path, header=list(range(i)), index_col=0)

            # write with cols
    msg = "cannot specify cols with a MultiIndex"
    with pytest.raises(TypeError, match=msg):
        df.to_csv(path, columns=["foo", "bar"])

with tm.ensure_clean("__tmp_to_csv_multiindex__") as path:
    # empty
    tsframe[:0].to_csv(path)
    recons = self.read_csv(path)

    exp = tsframe[:0]
    exp.index = []

    tm.assert_index_equal(recons.columns, exp.columns)
    assert len(recons) == 0
