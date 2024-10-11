# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
if read_ext == ".xlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Sheets containing datetimes not supported by pyxlsb"
        )
    )

parsed = pd.read_excel("test3" + read_ext, sheet_name="Sheet1")
expected = DataFrame([[np.nan]], columns=["Test"])
tm.assert_frame_equal(parsed, expected)
