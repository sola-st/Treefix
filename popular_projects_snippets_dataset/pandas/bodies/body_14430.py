# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py

with ensure_clean_store(setup_path) as store:

    index = Index([f"I am a very long string index: {i}" for i in range(20)])
    s = Series(np.arange(20), index=index)
    df = DataFrame({"A": s, "B": s})

    store["a"] = s
    tm.assert_series_equal(store["a"], s)

    store["b"] = df
    tm.assert_frame_equal(store["b"], df)

    # mixed length
    index = Index(
        ["abcdefghijklmnopqrstuvwxyz1234567890"]
        + [f"I am a very long string index: {i}" for i in range(20)]
    )
    s = Series(np.arange(21), index=index)
    df = DataFrame({"A": s, "B": s})
    store["a"] = s
    tm.assert_series_equal(store["a"], s)

    store["b"] = df
    tm.assert_frame_equal(store["b"], df)
