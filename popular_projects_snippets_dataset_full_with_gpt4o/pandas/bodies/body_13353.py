# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if self.mode in mode:
    expected = types_data_frame.astype({"DateCol": "datetime64[ns]"})

    result = read_sql(
        text,
        con=self.conn,
        parse_dates={
            "DateCol": {"errors": error},
        },
    )

    tm.assert_frame_equal(result, expected)
