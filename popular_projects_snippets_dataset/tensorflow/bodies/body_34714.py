# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
with self.cached_session():
    keys = constant_op.constant([11, 12, 13], dtypes.int64)
    values = constant_op.constant([0, 1, 2], dtypes.int64)
    table = lookup_ops.DenseHashTable(
        dtypes.int64,
        dtypes.int64,
        default_value=-1,
        empty_key=0,
        deleted_key=-1,
        experimental_is_anonymous=is_anonymous)

    self.evaluate(table.insert(keys, values))
    self.assertAllEqual(3, self.evaluate(table.size()))

    placeholder_keys = array_ops.placeholder(dtypes.int64)
    output = table.lookup(placeholder_keys)
    self.assertAllEqual(None, output.get_shape())
    result = output.eval({placeholder_keys: [11, 12, 15]})
    self.assertAllEqual([0, 1, -1], result)
