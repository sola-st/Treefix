# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:
    repr(store)
    store.info()
    store["a"] = tm.makeTimeSeries()
    store["b"] = tm.makeStringSeries()
    store["c"] = tm.makeDataFrame()

    df = tm.makeDataFrame()
    df["obj1"] = "foo"
    df["obj2"] = "bar"
    df["bool1"] = df["A"] > 0
    df["bool2"] = df["B"] > 0
    df["bool3"] = True
    df["int1"] = 1
    df["int2"] = 2
    df["timestamp1"] = Timestamp("20010102")
    df["timestamp2"] = Timestamp("20010103")
    df["datetime1"] = dt.datetime(2001, 1, 2, 0, 0)
    df["datetime2"] = dt.datetime(2001, 1, 3, 0, 0)
    df.loc[df.index[3:6], ["obj1"]] = np.nan
    df = df._consolidate()

    with catch_warnings(record=True):
        simplefilter("ignore", pd.errors.PerformanceWarning)
        store["df"] = df

    # make a random group in hdf space
    store._handle.create_group(store._handle.root, "bah")

    assert store.filename in repr(store)
    assert store.filename in str(store)
    store.info()

# storers
with ensure_clean_store(setup_path) as store:

    df = tm.makeDataFrame()
    store.append("df", df)

    s = store.get_storer("df")
    repr(s)
    str(s)
