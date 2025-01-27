# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-19242, gh-9155
#
# Test writing timedelta to xls.
df = DataFrame(
    np.random.randint(-10, 10, size=(20, 1)), columns=["A"], dtype=np.int64
)
expected = df.copy()

df["new"] = df["A"].apply(lambda x: timedelta(seconds=x))
expected["new"] = expected["A"].apply(
    lambda x: timedelta(seconds=x).total_seconds() / 86400
)

df.to_excel(path, "test1")
with ExcelFile(path) as reader:
    recons = pd.read_excel(reader, sheet_name="test1", index_col=0)
tm.assert_frame_equal(expected, recons)
