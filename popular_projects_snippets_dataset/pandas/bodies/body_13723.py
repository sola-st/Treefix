# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
ctx = styler.format_index({0: lambda v: v.upper()})._translate(True, True)
for i, val in enumerate(["X", "Y"]):
    assert ctx["body"][i][0]["display_value"] == val
