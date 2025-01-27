# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
xp = tsframe.resample("M", kind="period").mean()

xp.to_excel(path, "sht1")

with ExcelFile(path) as reader:
    rs = pd.read_excel(reader, sheet_name="sht1", index_col=0)
tm.assert_frame_equal(xp, rs.to_period("M"))
