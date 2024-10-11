# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 14194
# single unnamed index
ctx = df.style._translate(True, True)
assert ctx["body"][0][0]["is_visible"]
assert ctx["head"][0][0]["is_visible"]
ctx2 = df.style.hide(axis="index")._translate(True, True)
assert not ctx2["body"][0][0]["is_visible"]
assert not ctx2["head"][0][0]["is_visible"]

# single named index
ctx3 = df.set_index("A").style._translate(True, True)
assert ctx3["body"][0][0]["is_visible"]
assert len(ctx3["head"]) == 2  # 2 header levels
assert ctx3["head"][0][0]["is_visible"]

ctx4 = df.set_index("A").style.hide(axis="index")._translate(True, True)
assert not ctx4["body"][0][0]["is_visible"]
assert len(ctx4["head"]) == 1  # only 1 header levels
assert not ctx4["head"][0][0]["is_visible"]
