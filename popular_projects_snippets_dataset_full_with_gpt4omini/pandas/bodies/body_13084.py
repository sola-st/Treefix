# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Avoid mixed inferred_type.
df = DataFrame(
    [["\u0192", "\u0193", "\u0194"], ["\u0195", "\u0196", "\u0197"]],
    index=["A\u0192", "B"],
    columns=["X\u0193", "Y", "Z"],
)

with tm.ensure_clean("__tmp_to_excel_float_format__." + ext) as filename:
    df.to_excel(filename, sheet_name="TestSheet")
    result = pd.read_excel(filename, sheet_name="TestSheet", index_col=0)
    tm.assert_frame_equal(result, df)
