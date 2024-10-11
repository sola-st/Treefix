# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_formats.py
# GH#3869
ind = Index(["{other}%s", "~:{range}:0"], name="A")
result = ind._summary()
# shouldn't be formatted accidentally.
assert "~:{range}:0" in result
assert "{other}%s" in result
