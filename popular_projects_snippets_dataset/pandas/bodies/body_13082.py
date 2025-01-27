# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 19543.
expected = DataFrame([], columns=[0, 1, 2])

df = DataFrame([], index=MultiIndex.from_tuples([], names=[0, 1]), columns=[2])
df.to_excel(path, "test1")

with ExcelFile(path) as reader:
    result = pd.read_excel(reader, sheet_name="test1")
tm.assert_frame_equal(
    result, expected, check_index_type=False, check_dtype=False
)
