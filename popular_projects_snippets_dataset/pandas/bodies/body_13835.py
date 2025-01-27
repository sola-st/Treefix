# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 35607
df = DataFrame(data=[[0, 1], [1, 2]], columns=["A", "B"])
s = Styler(df, uuid_len=0)
s = s.set_table_styles({"A": [{"selector": "", "props": [("color", "blue")]}]})
assert "#T_ .col0 {\n  color: blue;\n}" in s.to_html()
s = s.set_table_styles(
    {0: [{"selector": "", "props": [("color", "blue")]}]}, axis=1
)
assert "#T_ .row0 {\n  color: blue;\n}" in s.to_html()
