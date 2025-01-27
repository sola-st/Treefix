# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
mi_styler.columns.names = ["zero", "one"]
if names:
    mi_styler.index.names = ["zero", "one"]
ctx = mi_styler.hide(axis="columns", level=level)._translate(True, False)
assert len(ctx["head"]) == (2 if names else 1)
