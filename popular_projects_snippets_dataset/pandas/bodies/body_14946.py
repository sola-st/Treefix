# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
# GH9012
rs = pc.convert([0, 1], None, axis)
xp = [0, 1]
assert rs == xp
