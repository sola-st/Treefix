# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame(123, index=range(10, 15), columns=range(30))

with option_context(
    "display.max_rows",
    10,
    "display.max_columns",
    40,
    "display.width",
    500,
    "display.expand_frame_repr",
    "info",
    "display.show_dimensions",
    True,
):
    assert "5 rows" in str(df)
    assert "5 rows" in df._repr_html_()
with option_context(
    "display.max_rows",
    10,
    "display.max_columns",
    40,
    "display.width",
    500,
    "display.expand_frame_repr",
    "info",
    "display.show_dimensions",
    False,
):
    assert "5 rows" not in str(df)
    assert "5 rows" not in df._repr_html_()
with option_context(
    "display.max_rows",
    2,
    "display.max_columns",
    2,
    "display.width",
    500,
    "display.expand_frame_repr",
    "info",
    "display.show_dimensions",
    "truncate",
):
    assert "5 rows" in str(df)
    assert "5 rows" in df._repr_html_()
with option_context(
    "display.max_rows",
    10,
    "display.max_columns",
    40,
    "display.width",
    500,
    "display.expand_frame_repr",
    "info",
    "display.show_dimensions",
    "truncate",
):
    assert "5 rows" not in str(df)
    assert "5 rows" not in df._repr_html_()
