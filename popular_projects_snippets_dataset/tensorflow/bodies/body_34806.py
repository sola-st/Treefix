# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = constant_op.constant([-1, -1], dtypes.int64)
keys = constant_op.constant(["brain", "salad", "surgery"])
table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

# Shape [6] instead of [3, 2]
values = constant_op.constant([0, 1, 2, 3, 4, 5], dtypes.int64)
with self.assertRaisesOpError("Expected shape"):
    self.evaluate(table.insert(keys, values))

# Shape [2,3] instead of [3, 2]
values = constant_op.constant([[0, 1, 2], [3, 4, 5]], dtypes.int64)
with self.assertRaisesOpError("Expected shape"):
    self.evaluate(table.insert(keys, values))

# Shape [2, 2] instead of [3, 2]
values = constant_op.constant([[0, 1], [2, 3]], dtypes.int64)
with self.assertRaisesOpError("Expected shape"):
    self.evaluate(table.insert(keys, values))

# Shape [3, 1] instead of [3, 2]
values = constant_op.constant([[0], [2], [4]], dtypes.int64)
with self.assertRaisesOpError("Expected shape"):
    self.evaluate(table.insert(keys, values))

# Valid Insert
values = constant_op.constant([[0, 1], [2, 3], [4, 5]], dtypes.int64)
self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))
