# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
styles = styler.set_table_styles(
    {"j": [{"selector": "td", "props": "a: v;"}]}, axis=1
).table_styles
assert styles == [
    {"selector": "td.row1", "props": [("a", "v")]},
    {"selector": "td.row2", "props": [("a", "v")]},
]
