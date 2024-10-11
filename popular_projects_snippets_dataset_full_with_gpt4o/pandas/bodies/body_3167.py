# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
with tm.ensure_clean("__tmp_to_csv_date_format__") as path:
    dt_index = datetime_frame.index
    datetime_frame = DataFrame(
        {"A": dt_index, "B": dt_index.shift(1)}, index=dt_index
    )
    datetime_frame.to_csv(path, date_format="%Y%m%d")

    # Check that the data was put in the specified format
    test = read_csv(path, index_col=0)

    datetime_frame_int = datetime_frame.applymap(
        lambda x: int(x.strftime("%Y%m%d"))
    )
    datetime_frame_int.index = datetime_frame_int.index.map(
        lambda x: int(x.strftime("%Y%m%d"))
    )

    tm.assert_frame_equal(test, datetime_frame_int)

    datetime_frame.to_csv(path, date_format="%Y-%m-%d")

    # Check that the data was put in the specified format
    test = read_csv(path, index_col=0)
    datetime_frame_str = datetime_frame.applymap(
        lambda x: x.strftime("%Y-%m-%d")
    )
    datetime_frame_str.index = datetime_frame_str.index.map(
        lambda x: x.strftime("%Y-%m-%d")
    )

    tm.assert_frame_equal(test, datetime_frame_str)

    # Check that columns get converted
    datetime_frame_columns = datetime_frame.T
    datetime_frame_columns.to_csv(path, date_format="%Y%m%d")

    test = read_csv(path, index_col=0)

    datetime_frame_columns = datetime_frame_columns.applymap(
        lambda x: int(x.strftime("%Y%m%d"))
    )
    # Columns don't get converted to ints by read_csv
    datetime_frame_columns.columns = datetime_frame_columns.columns.map(
        lambda x: x.strftime("%Y%m%d")
    )

    tm.assert_frame_equal(test, datetime_frame_columns)

    # test NaTs
    nat_index = to_datetime(
        ["NaT"] * 10 + ["2000-01-01", "2000-01-01", "2000-01-01"]
    )
    nat_frame = DataFrame({"A": nat_index}, index=nat_index)
    nat_frame.to_csv(path, date_format="%Y-%m-%d")

    test = read_csv(path, parse_dates=[0, 1], index_col=0)

    tm.assert_frame_equal(test, nat_frame)
