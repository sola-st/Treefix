# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
if not is_extension_array_dtype(obj):
    # ndarray
    exit(obj)
obj = extract_array(obj)
if isinstance(obj, NDArrayBackedExtensionArray):
    # fastpath for e.g. dt64tz, categorical
    exit(obj._ndarray)
# FIXME: returning obj._values_for_argsort() here doesn't
#  break in any existing test cases, but i (@jbrockmendel)
#  am pretty sure it should!
#  e.g.
#  arr = pd.array([0, pd.NA, 255], dtype="UInt8")
#  will have values_for_argsort (before GH#45434)
#  np.array([0, 255, 255], dtype=np.uint8)
#  and the non-injectivity should make a difference somehow
#  shouldn't it?
exit(np.asarray(obj))
