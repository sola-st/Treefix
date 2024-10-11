# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )
filename = "test1"
sheet_name = "Sheet1"

df1 = pd.read_excel(
    filename + read_ext, sheet_name=sheet_name, index_col=0
)  # doc
df2 = pd.read_excel(filename + read_ext, index_col=0, sheet_name=sheet_name)

tm.assert_frame_equal(df1, df_ref, check_names=False)
tm.assert_frame_equal(df2, df_ref, check_names=False)
