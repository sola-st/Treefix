# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
# GH 15492
df = DataFrame(
    {
        "date": ["2014-01-01", "2014-01-02"],
        "real_date": date_range("2014-01-01", periods=2),
        "float": [1.1, 1.2],
        "int": [1, 2],
    },
    columns=["date", "real_date", "float", "int"],
)

with ensure_clean_store(setup_path) as store:
    store.append("test", df, format="table", data_columns=True)

    ts = Timestamp("2014-01-01")  # noqa:F841
    result = store.select("test", where="real_date > ts")
    expected = df.loc[[1], :]
    tm.assert_frame_equal(expected, result)

    for op in ["<", ">", "=="]:
        # non strings to string column always fail
        for v in [2.1, True, Timestamp("2014-01-01"), pd.Timedelta(1, "s")]:
            query = f"date {op} v"
            msg = f"Cannot compare {v} of type {type(v)} to string column"
            with pytest.raises(TypeError, match=msg):
                store.select("test", where=query)

            # strings to other columns must be convertible to type
        v = "a"
        for col in ["int", "float", "real_date"]:
            query = f"{col} {op} v"
            if col == "real_date":
                msg = 'Given date string "a" not likely a datetime'
            else:
                msg = "could not convert string to "
            with pytest.raises(ValueError, match=msg):
                store.select("test", where=query)

        for v, col in zip(
            ["1", "1.1", "2014-01-01"], ["int", "float", "real_date"]
        ):
            query = f"{col} {op} v"
            result = store.select("test", where=query)

            if op == "==":
                expected = df.loc[[0], :]
            elif op == ">":
                expected = df.loc[[1], :]
            else:
                expected = df.loc[[], :]
            tm.assert_frame_equal(expected, result)
