# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
styler.set_table_styles(
    [
        {"selector": "toprule", "props": ":value"},
        {"selector": "bottomrule", "props": ":value"},
        {"selector": "midrule", "props": ":value"},
        {"selector": "column_format", "props": ":value"},
    ]
)
assert _parse_latex_table_wrapping(styler.table_styles, styler.caption) is False
assert _parse_latex_table_wrapping(styler.table_styles, "some caption") is True
styler.set_table_styles(
    [
        {"selector": "not-ignored", "props": ":value"},
    ],
    overwrite=False,
)
assert _parse_latex_table_wrapping(styler.table_styles, None) is True
