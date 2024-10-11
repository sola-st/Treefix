# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_formats.py
# GH32146
arr = Index([True, False, np.nan], dtype=object)
exp1 = arr.format()
out1 = ["True", "False", "NaN"]
assert out1 == exp1

exp2 = repr(arr)
out2 = "Index([True, False, nan], dtype='object')"
assert out2 == exp2
