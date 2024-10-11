# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
arrays = np.arange(len(frame.index) * 2, dtype=np.int64).reshape(2, -1)
new_index = MultiIndex.from_arrays(arrays, names=["first", "second"])
frame.index = new_index

new_cols_index = MultiIndex.from_tuples([(40, 1), (40, 2), (50, 1), (50, 2)])
frame.columns = new_cols_index
header = [0, 1]
if not merge_cells:
    header = 0

# round trip
frame.to_excel(path, "test1", merge_cells=merge_cells)
with ExcelFile(path) as reader:
    df = pd.read_excel(
        reader, sheet_name="test1", header=header, index_col=[0, 1]
    )
if not merge_cells:
    fm = frame.columns.format(sparsify=False, adjoin=False, names=False)
    frame.columns = [".".join(map(str, q)) for q in zip(*fm)]
tm.assert_frame_equal(frame, df)
