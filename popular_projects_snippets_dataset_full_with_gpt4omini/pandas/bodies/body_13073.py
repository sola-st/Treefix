# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-19242
#
# Test writing Interval without labels.
df = DataFrame(np.random.randint(-10, 10, size=(20, 1)), dtype=np.int64)
expected = df.copy()

df["new"] = pd.cut(df[0], 10)
expected["new"] = pd.cut(expected[0], 10).astype(str)

df.to_excel(path, "test1")
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)
tm.assert_frame_equal(expected, recons)
