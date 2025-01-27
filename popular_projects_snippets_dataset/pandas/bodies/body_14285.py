# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

# GH 4096; using same frames, but different block orderings
with ensure_clean_store(setup_path) as store:

    for i in range(10):

        df = DataFrame(np.random.randn(10, 2), columns=list("AB"))
        df["index"] = range(10)
        df["index"] += i * 10
        df["int64"] = Series([1] * len(df), dtype="int64")
        df["int16"] = Series([1] * len(df), dtype="int16")

        if i % 2 == 0:
            del df["int64"]
            df["int64"] = Series([1] * len(df), dtype="int64")
        if i % 3 == 0:
            a = df.pop("A")
            df["A"] = a

        df.set_index("index", inplace=True)

        store.append("df", df)

    # test a different ordering but with more fields (like invalid
    # combinations)
with ensure_clean_store(setup_path) as store:

    df = DataFrame(np.random.randn(10, 2), columns=list("AB"), dtype="float64")
    df["int64"] = Series([1] * len(df), dtype="int64")
    df["int16"] = Series([1] * len(df), dtype="int16")
    store.append("df", df)

    # store additional fields in different blocks
    df["int16_2"] = Series([1] * len(df), dtype="int16")
    msg = re.escape(
        "cannot match existing table structure for [int16] on appending data"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)

    # store multiple additional fields in different blocks
    df["float_3"] = Series([1.0] * len(df), dtype="float64")
    msg = re.escape(
        "cannot match existing table structure for [A,B] on appending data"
    )
    with pytest.raises(ValueError, match=msg):
        store.append("df", df)
