# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Test np.float values read come back as float.
df = DataFrame(np.random.random_sample(10), dtype=np_type)
df.to_excel(path, "test1")

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0).astype(
        np_type
    )

tm.assert_frame_equal(df, recons)
