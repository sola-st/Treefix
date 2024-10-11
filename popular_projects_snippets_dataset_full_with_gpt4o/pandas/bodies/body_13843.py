# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
mi_df.columns.names = ["Lev0", "Lev1"]
mi_styler = mi_df.style
ctx = mi_styler._translate(True, True)
assert ctx["head"][0][1]["display_value"] == "Lev0"
assert ctx["head"][1][1]["display_value"] == "Lev1"

mi_styler.hide(names=True, axis="columns")
ctx = mi_styler._translate(True, True)
assert ctx["head"][0][1]["display_value"] == "&nbsp;"
assert ctx["head"][1][1]["display_value"] == "&nbsp;"

mi_styler.hide(level=0, axis="columns")
ctx = mi_styler._translate(True, True)
assert len(ctx["head"]) == 1  # no index names and only one visible column headers
assert ctx["head"][0][1]["display_value"] == "&nbsp;"
