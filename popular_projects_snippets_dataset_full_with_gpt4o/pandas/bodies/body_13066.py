# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
df = DataFrame([(1, np.inf), (2, 3), (5, -np.inf)])
df.to_excel(path, "test1")

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)

tm.assert_frame_equal(df, recons)
