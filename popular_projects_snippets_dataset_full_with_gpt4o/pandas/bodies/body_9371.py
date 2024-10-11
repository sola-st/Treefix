# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_comparison.py
# GH-30652
# equals is generally tested in /tests/extension/base/methods, but this
# specifically tests that two arrays of the same class but different dtype
# do not evaluate equal
a1 = pd.array([1, 2, None], dtype="Int64")
a2 = pd.array([1, 2, None], dtype="Int32")
assert a1.equals(a2) is False
