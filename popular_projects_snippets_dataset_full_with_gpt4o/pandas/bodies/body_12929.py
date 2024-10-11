# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 38956, 39001 - no/incorrect dimension information
path = datapath("io", "data", "excel", f"{filename}{ext}")
if read_only is None:
    result = pd.read_excel(path, header=header)
else:
    with contextlib.closing(
        openpyxl.load_workbook(path, read_only=read_only)
    ) as wb:
        result = pd.read_excel(wb, engine="openpyxl", header=header)
expected = DataFrame(expected_data)
tm.assert_frame_equal(result, expected)
