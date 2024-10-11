# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_openpyxl.py
# GH 39528
filename = datapath("io", "data", "excel", "test1" + ext)
with contextlib.closing(
    openpyxl.load_workbook(filename, read_only=read_only)
) as wb:
    result = pd.read_excel(wb, engine="openpyxl")
expected = pd.read_excel(filename)
tm.assert_frame_equal(result, expected)
