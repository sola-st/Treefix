# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

df1 = df_ref.reindex(columns=["A", "B", "C"])
df2 = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols="A:D"
)
df3 = pd.read_excel(
    "test1" + read_ext,
    sheet_name="Sheet2",
    skiprows=[1],
    index_col=0,
    usecols="A:D",
)

# TODO add index to xls, read xls ignores index name ?
tm.assert_frame_equal(df2, df1, check_names=False)
tm.assert_frame_equal(df3, df1, check_names=False)

df1 = df_ref.reindex(columns=["B", "C"])
df2 = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols="A,C,D"
)
df3 = pd.read_excel(
    "test1" + read_ext,
    sheet_name="Sheet2",
    skiprows=[1],
    index_col=0,
    usecols="A,C,D",
)
# TODO add index to xls file
tm.assert_frame_equal(df2, df1, check_names=False)
tm.assert_frame_equal(df3, df1, check_names=False)

df1 = df_ref.reindex(columns=["B", "C"])
df2 = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols="A,C:D"
)
df3 = pd.read_excel(
    "test1" + read_ext,
    sheet_name="Sheet2",
    skiprows=[1],
    index_col=0,
    usecols="A,C:D",
)
tm.assert_frame_equal(df2, df1, check_names=False)
tm.assert_frame_equal(df3, df1, check_names=False)
