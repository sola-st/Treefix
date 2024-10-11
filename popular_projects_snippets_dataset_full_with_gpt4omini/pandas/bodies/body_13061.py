# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
df = tsframe

# freq doesn't round-trip
index = pd.DatetimeIndex(np.asarray(df.index), freq=None)
df.index = index

df.to_excel(path, "test1")
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)
tm.assert_frame_equal(df, recons)
