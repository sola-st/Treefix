# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
ctx = styler.format(lambda v: "neg" if v < 0 else "pos")._translate(True, True)
assert ctx["body"][0][1]["display_value"] == "pos"
assert ctx["body"][0][2]["display_value"] == "neg"
assert ctx["body"][1][1]["display_value"] == "pos"
assert ctx["body"][1][2]["display_value"] == "neg"
