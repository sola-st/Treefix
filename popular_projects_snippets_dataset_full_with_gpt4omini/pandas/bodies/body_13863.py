# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
styles = styler.set_table_styles(
    {"d": [{"selector": "td", "props": "a: v;"}]}, axis=0
).table_styles
assert styles == [
    {"selector": "td.col1", "props": [("a", "v")]},
    {"selector": "td.col2", "props": [("a", "v")]},
]
