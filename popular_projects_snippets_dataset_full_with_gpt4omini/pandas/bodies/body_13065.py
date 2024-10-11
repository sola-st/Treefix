# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Test np.bool_ values read come back as float.
df = DataFrame([1, 0, True, False], dtype=np.bool_)
df.to_excel(path, "test1")

with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0).astype(
        np.bool_
    )

tm.assert_frame_equal(df, recons)
