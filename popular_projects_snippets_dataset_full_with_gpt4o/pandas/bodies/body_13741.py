# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
styler = Styler(df, precision=0)
ctx = styler._translate(True, True)
assert ctx["body"][0][2]["display_value"] == "-1"
assert ctx["body"][1][2]["display_value"] == "-1"
