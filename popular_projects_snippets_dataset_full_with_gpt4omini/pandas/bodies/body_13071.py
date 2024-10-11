# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# datetime.date, not sure what to test here exactly

# freq does not round-trip
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
tsframe.index = index

tsf = tsframe.copy()

tsf.index = [x.date() for x in tsframe.index]
tsf.to_excel(path, "test1", merge_cells=merge_cells)

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)

tm.assert_frame_equal(tsframe, recons)
