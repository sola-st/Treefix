# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

# frame
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

with ensure_clean_store(setup_path) as store:
    store.append("df1_mixed", df)
    tm.assert_frame_equal(store.select("df1_mixed"), df)
