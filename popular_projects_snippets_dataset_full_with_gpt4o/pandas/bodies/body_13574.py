# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame({r"Design": [1, 2, 3], r"ratio": [4, 5, 6], r"xy": [10, 11, 12]})
row_string_converter = RowStringConverter(
    formatter=DataFrameFormatter(df, escape=True),
)
assert row_string_converter.get_strrow(row_num=row_num) == expected
