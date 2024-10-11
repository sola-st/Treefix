# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_non_unique.py
# GH 41269
if func == "apply":
    op = lambda s: ["color: red;"] * len(s)
else:
    op = lambda v: "color: red;"

with pytest.raises(KeyError, match="`Styler.apply` and `.applymap` are not"):
    getattr(df.style, func)(op)._compute()
