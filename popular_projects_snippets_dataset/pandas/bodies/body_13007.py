# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH 41448
if engine == "odf":
    pytest.skip("chartsheets do not exist in the ODF format")
if engine == "pyxlsb":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="pyxlsb can't distinguish chartsheets from worksheets"
        )
    )
with pytest.raises(ValueError, match="Worksheet named 'Chart1' not found"):
    pd.read_excel("chartsheet" + read_ext, sheet_name="Chart1")
