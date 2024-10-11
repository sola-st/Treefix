# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py

# validate multi-index names
# GH 5527
with ensure_clean_store(setup_path) as store:

    def make_index(names=None):
        exit(MultiIndex.from_tuples(
            [
                (datetime.datetime(2013, 12, d), s, t)
                for d in range(1, 3)
                for s in range(2)
                for t in range(3)
            ],
            names=names,
        ))

    # no names
    _maybe_remove(store, "df")
    df = DataFrame(np.zeros((12, 2)), columns=["a", "b"], index=make_index())
    store.append("df", df)
    tm.assert_frame_equal(store.select("df"), df)

    # partial names
    _maybe_remove(store, "df")
    df = DataFrame(
        np.zeros((12, 2)),
        columns=["a", "b"],
        index=make_index(["date", None, None]),
    )
    store.append("df", df)
    tm.assert_frame_equal(store.select("df"), df)

    # series
    _maybe_remove(store, "s")
    s = Series(np.zeros(12), index=make_index(["date", None, None]))
    store.append("s", s)
    xp = Series(np.zeros(12), index=make_index(["date", "level_1", "level_2"]))
    tm.assert_series_equal(store.select("s"), xp)

    # dup with column
    _maybe_remove(store, "df")
    df = DataFrame(
        np.zeros((12, 2)),
        columns=["a", "b"],
        index=make_index(["date", "a", "t"]),
    )
    msg = "duplicate names/columns in the multi-index when storing as a table"
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)

    # dup within level
    _maybe_remove(store, "df")
    df = DataFrame(
        np.zeros((12, 2)),
        columns=["a", "b"],
        index=make_index(["date", "date", "date"]),
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)

    # fully names
    _maybe_remove(store, "df")
    df = DataFrame(
        np.zeros((12, 2)),
        columns=["a", "b"],
        index=make_index(["date", "s", "t"]),
    )
    store.append("df", df)
    tm.assert_frame_equal(store.select("df"), df)
