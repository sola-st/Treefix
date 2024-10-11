# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
df = DataFrame(
    [[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]],
    index=["A", "B"],
    columns=["X", "Y", "Z"],
)
df.to_excel(path, "test1", float_format="%.2f")

with ExcelFile(path) as reader:
    result = pd.read_excel(reader, sheet_name="test1", index_col=0)

expected = DataFrame(
    [[0.12, 0.23, 0.57], [12.32, 123123.20, 321321.20]],
    index=["A", "B"],
    columns=["X", "Y", "Z"],
)
tm.assert_frame_equal(result, expected)
