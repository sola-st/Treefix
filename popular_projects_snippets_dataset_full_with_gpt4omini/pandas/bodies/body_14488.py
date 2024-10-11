# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py

with ensure_clean_store(setup_path) as store:

    dtypes = [("date", datetime.date(2001, 1, 2))]

    # currently not supported dtypes ####
    for n, f in dtypes:
        df = tm.makeDataFrame()
        df[n] = f
        msg = re.escape(f"[{n}] is not implemented as a table column")
        with pytest.raises(TypeError, match=msg):
            store.append(f"df1_{n}", df)

    # frame
df = tm.makeDataFrame()
df["obj1"] = "foo"
df["obj2"] = "bar"
df["datetime1"] = datetime.date(2001, 1, 2)
df = df._consolidate()

with ensure_clean_store(setup_path) as store:
    # this fails because we have a date in the object block......
    msg = re.escape(
        """Cannot serialize the column [datetime1]
because its data contents are not [string] but [date] object dtype"""
    )
    with pytest.raises(TypeError, match=msg):
        store.append("df_unimplemented", df)
