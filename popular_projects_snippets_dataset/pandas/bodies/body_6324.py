# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
# in practice we will not typically call this with a 1-length list
# (we shortcut to just use that dtype as the common dtype), but
# still testing as good practice to have this working (and it is the
# only case we can test in general)
assert dtype._get_common_dtype([dtype]) == dtype
