# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

df_ref = df_ref.reindex(columns=["B", "C"])
df1 = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols=[0, 2, 3]
)
df2 = pd.read_excel(
    "test1" + read_ext,
    sheet_name="Sheet2",
    skiprows=[1],
    index_col=0,
    usecols=[0, 2, 3],
)

# TODO add index to xls file)
tm.assert_frame_equal(df1, df_ref, check_names=False)
tm.assert_frame_equal(df2, df_ref, check_names=False)
