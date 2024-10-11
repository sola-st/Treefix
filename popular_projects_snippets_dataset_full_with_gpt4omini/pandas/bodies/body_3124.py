# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean("__tmp_to_csv_from_csv4__") as path:
    # GH 10833 (TimedeltaIndex formatting)
    dt = pd.Timedelta(seconds=1)
    df = DataFrame(
        {"dt_data": [i * dt for i in range(3)]},
        index=Index([i * dt for i in range(3)], name="dt_index"),
    )
    df.to_csv(path)

    result = read_csv(path, index_col="dt_index")
    result.index = pd.to_timedelta(result.index)
    result["dt_data"] = pd.to_timedelta(result["dt_data"])

    tm.assert_frame_equal(df, result, check_index_type=True)
