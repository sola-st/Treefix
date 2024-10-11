# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
ctx = styler.format("{:0.1f}")._translate(True, True)
assert all(["display_value" in c for c in row] for row in ctx["body"])
assert all([len(c["display_value"]) <= 3 for c in row[1:]] for row in ctx["body"])
assert len(ctx["body"][0][1]["display_value"].lstrip("-")) <= 3
