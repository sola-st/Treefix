# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 31677
write_frame = DataFrame({"A": [1, 1, 1], "B": [2, 2, 2], "C": [3, 3, 3]})
write_frame.to_excel(
    path, "col_subset_bug", columns=["A", "B"], index=to_excel_index
)

expected = write_frame[["A", "B"]]
read_frame = pd.read_excel(
    path, sheet_name="col_subset_bug", index_col=read_excel_index_col
)

tm.assert_frame_equal(expected, read_frame)
