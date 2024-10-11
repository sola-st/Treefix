# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
styler.relabel_index(["{}", "{}"])
ctx = styler._translate(True, True)
assert {"value": "x", "display_value": "x"}.items() <= ctx["body"][0][0].items()
assert {"value": "y", "display_value": "y"}.items() <= ctx["body"][1][0].items()
