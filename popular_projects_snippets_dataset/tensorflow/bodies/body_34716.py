# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
for float_dtype in [dtypes.float32, dtypes.float64]:
    keys = constant_op.constant([11, 12, 13, 14], dtypes.int64)
    values = constant_op.constant([0.0, 1.1, 2.2, 3.3], float_dtype)
    default_value = constant_op.constant(-1.5, float_dtype)
    table = lookup_ops.DenseHashTable(
        dtypes.int64,
        float_dtype,
        default_value=default_value,
        empty_key=0,
        deleted_key=-1,
        experimental_is_anonymous=is_anonymous)
    self.assertAllEqual(0, self.evaluate(table.size()))

    self.evaluate(table.insert(keys, values))
    self.assertAllEqual(4, self.evaluate(table.size()))

    remove_string = constant_op.constant([12, 15], dtypes.int64)
    self.evaluate(table.remove(remove_string))
    self.assertAllEqual(3, self.evaluate(table.size()))

    input_string = constant_op.constant([11, 12, 14, 15], dtypes.int64)
    output = table.lookup(input_string)
    self.assertAllEqual([4], output.get_shape())

    result = self.evaluate(output)
    self.assertAllClose([0, -1.5, 3.3, -1.5], result)
