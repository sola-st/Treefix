# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

with ensure_clean_store(setup_path) as store:

    df = DataFrame({"cols": range(6), "values": range(6)}, dtype="float64")
    df["cols"] = (df["cols"] + 10).apply(str)
    df.iloc[0] = np.nan

    expected = DataFrame(
        {"cols": ["13.0", "14.0", "15.0"], "values": [3.0, 4.0, 5.0]},
        index=[3, 4, 5],
    )

    # write w/o the index on that particular column
    store.append("df", df, data_columns=True, index=["cols"])
    result = store.select("df", where="values>2.0")
    tm.assert_frame_equal(result, expected)
