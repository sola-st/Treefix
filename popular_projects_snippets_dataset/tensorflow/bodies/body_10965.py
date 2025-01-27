# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
# TODO(gunan) Reenable after this issue is fixed:
# https://github.com/google/protobuf/issues/2812
if sys.version_info >= (3, 5):
    self.skipTest("Skipped test for Python 3.5+")

# Smaller than the threshold: no warning.
c_sparse = indexed_slices.IndexedSlices(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(dtypes.int32), constant([4, 4, 4, 4]))
with warnings.catch_warnings(record=True) as w:
    math_ops.multiply(c_sparse, 1.0)
self.assertEqual(0, len(w))

# Greater than or equal to the threshold: warning.
c_sparse = indexed_slices.IndexedSlices(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(dtypes.int32), constant([100, 100, 100, 100]))
# "always" filter prevents the warning from being suppressed if it was
# already triggered in a different test.
warnings.simplefilter("always")
with warnings.catch_warnings(record=True) as w:
    math_ops.multiply(c_sparse, 1.0)
self.assertEqual(1, len(w))
self.assertIn(
    "with 100000000 elements. This may consume a large amount of memory.",
    str(w[0].message))

# Unknown dense shape: warning.
c_sparse = indexed_slices.IndexedSlices(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(dtypes.int32),
    array_ops.placeholder(dtypes.int32))
with warnings.catch_warnings(record=True) as w:
    math_ops.multiply(c_sparse, 1.0)
self.assertEqual(1, len(w))
self.assertIn(
    "of unknown shape. This may consume a large amount of memory.",
    str(w[0].message))
