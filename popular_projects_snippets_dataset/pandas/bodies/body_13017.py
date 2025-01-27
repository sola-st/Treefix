# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
pth = "test1" + read_ext
expected = pd.read_excel(pth, sheet_name="Sheet1", index_col=0, engine=engine)

with open(pth, "rb") as f:
    with pd.ExcelFile(f) as xls:
        actual = pd.read_excel(xls, sheet_name="Sheet1", index_col=0)

tm.assert_frame_equal(expected, actual)
