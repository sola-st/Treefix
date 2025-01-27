# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
# gh 46384: booleans do not collapse to integer representation on display
df = DataFrame([[True, False]])
ctx = df.style._translate(True, True)
assert ctx["body"][0][1]["display_value"] is True
assert ctx["body"][0][2]["display_value"] is False
