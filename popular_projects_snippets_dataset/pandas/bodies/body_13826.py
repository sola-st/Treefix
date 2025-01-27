# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 14194
# test hiding single column
ctx = df.style._translate(True, True)
assert ctx["head"][0][1]["is_visible"]
assert ctx["head"][0][1]["display_value"] == "A"
assert ctx["head"][0][2]["is_visible"]
assert ctx["head"][0][2]["display_value"] == "B"
assert ctx["body"][0][1]["is_visible"]  # col A, row 1
assert ctx["body"][1][2]["is_visible"]  # col B, row 1

ctx = df.style.hide("A", axis="columns")._translate(True, True)
assert not ctx["head"][0][1]["is_visible"]
assert not ctx["body"][0][1]["is_visible"]  # col A, row 1
assert ctx["body"][1][2]["is_visible"]  # col B, row 1

# test hiding mulitiple columns
ctx = df.style.hide(["A", "B"], axis="columns")._translate(True, True)
assert not ctx["head"][0][1]["is_visible"]
assert not ctx["head"][0][2]["is_visible"]
assert not ctx["body"][0][1]["is_visible"]  # col A, row 1
assert not ctx["body"][1][2]["is_visible"]  # col B, row 1
