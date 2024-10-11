# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# try multiindex with dates
new_index = [tsframe.index, np.arange(len(tsframe.index), dtype=np.int64)]
tsframe.index = MultiIndex.from_arrays(new_index)

tsframe.index.names = ["time", "foo"]
tsframe.to_excel(path, "test1", merge_cells=merge_cells)
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=[0, 1])

tm.assert_frame_equal(tsframe, recons)
assert recons.index.names == ("time", "foo")
