# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

filename = "test1"
sheet_name = "Sheet1"

with pd.ExcelFile(filename + read_ext) as excel:
    df1_parse = excel.parse(sheet_name=sheet_name, index_col=0)  # doc

with pd.ExcelFile(filename + read_ext) as excel:
    df2_parse = excel.parse(index_col=0, sheet_name=sheet_name)

tm.assert_frame_equal(df1_parse, df_ref, check_names=False)
tm.assert_frame_equal(df2_parse, df_ref, check_names=False)
