# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-4133
#
# Excel output format strings
df = DataFrame(
    [
        [date(2014, 1, 31), date(1999, 9, 24)],
        [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ],
    index=["DATE", "DATETIME"],
    columns=["X", "Y"],
)
df_expected = DataFrame(
    [
        [datetime(2014, 1, 31), datetime(1999, 9, 24)],
        [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ],
    index=["DATE", "DATETIME"],
    columns=["X", "Y"],
)

with tm.ensure_clean(ext) as filename2:
    with ExcelWriter(path) as writer1:
        df.to_excel(writer1, "test1")

    with ExcelWriter(
        filename2,
        date_format="DD.MM.YYYY",
        datetime_format="DD.MM.YYYY HH-MM-SS",
    ) as writer2:
        df.to_excel(writer2, "test1")

    with ExcelFile(path) as reader1:
        rs1 = pd.read_excel(reader1, sheet_name="test1", index_col=0)

    with ExcelFile(filename2) as reader2:
        rs2 = pd.read_excel(reader2, sheet_name="test1", index_col=0)

tm.assert_frame_equal(rs1, rs2)

# Since the reader returns a datetime object for dates,
# we need to use df_expected to check the result.
tm.assert_frame_equal(rs2, df_expected)
