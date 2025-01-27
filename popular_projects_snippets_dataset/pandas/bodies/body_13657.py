# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
result = styler_mi.to_html(
    max_rows=2 if rows else None,
    max_columns=2 if cols else None,
)

assert ">5</td>" in result  # [[0,1], [4,5]] always visible
assert (">8</td>" in result) is not rows  # first trimmed vertical element
assert (">2</td>" in result) is not cols  # first trimmed horizontal element
