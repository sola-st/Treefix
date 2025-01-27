# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 39396
s = Styler(df, uuid_len=0).applymap(lambda x: "color: red;", subset=["A"])
s.to_html()  # do 2 renders to ensure css styles not duplicated
assert (
    '<style type="text/css">\n#T__row0_col0, #T__row1_col0 {\n'
    "  color: red;\n}\n</style>" in s.to_html()
)
