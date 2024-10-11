# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
mixed_frame = frame.copy()
mixed_frame["foo"] = "bar"

mixed_frame.to_excel(path, "test1")
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)
tm.assert_frame_equal(mixed_frame, recons)
