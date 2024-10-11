# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

expected = df_ref[["A", "C"]]
result = pd.read_excel(
    "test1" + read_ext, sheet_name="Sheet1", index_col=0, usecols=usecols
)
tm.assert_frame_equal(result, expected, check_names=False)
