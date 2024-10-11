# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
with ExcelWriter(path) as writer:
    frame.to_excel(writer, "Data1")
    frame2 = frame.copy()
    frame2.columns = frame.columns[::-1]
    frame2.to_excel(writer, "Data2")

with ExcelFile(path) as reader:
    found_df = pd.read_excel(reader, sheet_name="Data1", index_col=0)
    found_df2 = pd.read_excel(reader, sheet_name="Data2", index_col=0)

    tm.assert_frame_equal(found_df, frame)
    tm.assert_frame_equal(found_df2, frame2)
