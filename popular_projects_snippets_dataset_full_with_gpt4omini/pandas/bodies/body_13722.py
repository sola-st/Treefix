# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
ctx = styler.format({"A": "{:0.1f}", "B": "{0:.2%}"})._translate(True, True)
assert ctx["body"][0][1]["display_value"] == "0.0"
assert ctx["body"][0][2]["display_value"] == "-60.90%"
