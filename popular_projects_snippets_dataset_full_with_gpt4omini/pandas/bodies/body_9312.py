# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH 9347, 9190
cat = Categorical([0, 1, 2], ordered=ordered)
assert cat.ordered == bool(ordered)
