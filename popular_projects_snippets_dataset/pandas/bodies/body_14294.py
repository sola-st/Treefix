# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
# empty frame, GH4273
with ensure_clean_store(setup_path) as store:

    # 0 len
    df_empty = DataFrame(columns=list("ABC"))
    store.append("df", df_empty)
    with pytest.raises(KeyError, match="'No object named df in the file'"):
        store.select("df")

    # repeated append of 0/non-zero frames
    df = DataFrame(np.random.rand(10, 3), columns=list("ABC"))
    store.append("df", df)
    tm.assert_frame_equal(store.select("df"), df)
    store.append("df", df_empty)
    tm.assert_frame_equal(store.select("df"), df)

    # store
    df = DataFrame(columns=list("ABC"))
    store.put("df2", df)
    tm.assert_frame_equal(store.select("df2"), df)
