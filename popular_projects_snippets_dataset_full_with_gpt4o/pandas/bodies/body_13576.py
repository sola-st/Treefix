# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame(
    {
        ("c1", 0): {x: x for x in range(5)},
        ("c1", 1): {x: x + 5 for x in range(5)},
        ("c2", 0): {x: x for x in range(5)},
        ("c2", 1): {x: x + 5 for x in range(5)},
        ("c3", 0): {x: x for x in range(5)},
    }
)

row_string_converter = RowStringConverter(
    formatter=DataFrameFormatter(df),
    multicolumn=True,
    multicolumn_format="r",
    multirow=True,
)

assert row_string_converter.get_strrow(row_num=row_num) == expected
