# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 46988 - openpyxl returns this sheet with floats
path = datapath("io", "data", "excel", f"ints_spelled_with_decimals{ext}")
result = pd.read_excel(path)
expected = DataFrame(range(2, 12), columns=[1])
tm.assert_frame_equal(result, expected)
