# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Test np.int values read come back as int
# (rather than float which is Excel's format).
df = DataFrame(np.random.randint(-10, 10, size=(10, 2)), dtype=np_type)
df.to_excel(path, "test1")

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)

int_frame = df.astype(np.int64)
tm.assert_frame_equal(int_frame, recons)

recons2 = pd.read_excel(path, sheet_name="test1", index_col=0)
tm.assert_frame_equal(int_frame, recons2)
