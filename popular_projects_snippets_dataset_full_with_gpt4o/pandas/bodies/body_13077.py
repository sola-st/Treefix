# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
arrays = np.arange(len(frame.index) * 2, dtype=np.int64).reshape(2, -1)
new_index = MultiIndex.from_arrays(arrays, names=["first", "second"])
frame.index = new_index

frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", columns=["A", "B"])

# round trip
frame.to_excel(path, "test1", merge_cells=merge_cells)
with ExcelFile(path) as reader:
    df = pd.read_excel(reader, sheet_name="test1", index_col=[0, 1])
tm.assert_frame_equal(frame, df)
