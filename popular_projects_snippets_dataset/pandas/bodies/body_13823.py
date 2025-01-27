# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
ctx = styler.hide(axis="columns")._translate(True, True)
assert len(ctx["head"]) == 0  # no header entries with an unnamed index

df.index.name = "some_name"
ctx = df.style.hide(axis="columns")._translate(True, True)
assert len(ctx["head"]) == 1
