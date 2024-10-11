# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 10875
index = Index(arg, name="label")
assert index.name == dt_conv(index).name
