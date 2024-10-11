# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
ctx = styler.format("{:.2f}")._translate(True, True)
assert ctx["body"][0][1]["display_value"] == "0.00"
assert ctx["body"][0][2]["display_value"] == "-0.61"
assert ctx["body"][1][1]["display_value"] == "1.00"
assert ctx["body"][1][2]["display_value"] == "-1.23"
