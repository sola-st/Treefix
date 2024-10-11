# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py

expected = DataFrame.from_records(
    [
        (
            datetime(2006, 11, 19, 23, 13, 20),
            1479596223000,
            datetime(2010, 1, 20),
            datetime(2010, 1, 8),
            datetime(2010, 1, 1),
            datetime(1974, 7, 1),
            datetime(2010, 1, 1),
            datetime(2010, 1, 1),
        ),
        (
            datetime(1959, 12, 31, 20, 3, 20),
            -1479590,
            datetime(1953, 10, 2),
            datetime(1948, 6, 10),
            datetime(1955, 1, 1),
            datetime(1955, 7, 1),
            datetime(1955, 1, 1),
            datetime(2, 1, 1),
        ),
        (pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT),
    ],
    columns=[
        "datetime_c",
        "datetime_big_c",
        "date",
        "weekly_date",
        "monthly_date",
        "quarterly_date",
        "half_yearly_date",
        "yearly_date",
    ],
)
expected["yearly_date"] = expected["yearly_date"].astype("O")

with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    parsed_114 = self.read_dta(
        datapath("io", "data", "stata", "stata2_114.dta")
    )
    parsed_115 = self.read_dta(
        datapath("io", "data", "stata", "stata2_115.dta")
    )
    parsed_117 = self.read_dta(
        datapath("io", "data", "stata", "stata2_117.dta")
    )
    # 113 is buggy due to limits of date format support in Stata
    # parsed_113 = self.read_dta(
    # datapath("io", "data", "stata", "stata2_113.dta")
    # )

    # Remove resource warnings
    w = [x for x in w if x.category is UserWarning]

    # should get warning for each call to read_dta
    assert len(w) == 3

# buggy test because of the NaT comparison on certain platforms
# Format 113 test fails since it does not support tc and tC formats
# tm.assert_frame_equal(parsed_113, expected)
tm.assert_frame_equal(parsed_114, expected, check_datetimelike_compat=True)
tm.assert_frame_equal(parsed_115, expected, check_datetimelike_compat=True)
tm.assert_frame_equal(parsed_117, expected, check_datetimelike_compat=True)
