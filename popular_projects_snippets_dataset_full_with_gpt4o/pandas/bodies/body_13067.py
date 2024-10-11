# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py

# freq doesn't round-trip
index = pd.DatetimeIndex(np.asarray(tsframe.index), freq=None)
tsframe.index = index

frame = frame.copy()
frame.iloc[:5, frame.columns.get_loc("A")] = np.nan

frame.to_excel(path, "test1")
frame.to_excel(path, "test1", columns=["A", "B"])
frame.to_excel(path, "test1", header=False)
frame.to_excel(path, "test1", index=False)

# Test writing to separate sheets
with ExcelWriter(path) as writer:
    frame.to_excel(writer, "test1")
    tsframe.to_excel(writer, "test2")
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)
    tm.assert_frame_equal(frame, recons)
    recons = pd.read_excel(reader, sheet_name="test2", index_col=0)
    tm.assert_frame_equal(tsframe, recons)
assert 2 == len(reader.sheet_names)
assert "test1" == reader.sheet_names[0]
assert "test2" == reader.sheet_names[1]
