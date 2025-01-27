# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
keys = constant_op.constant(["a", "b", "c", "d"], dtypes.string)
values = constant_op.constant([0.0, 1.1, 2.2, 3.3], dtypes.float32)
default_value = constant_op.constant(-1.5, dtypes.float32)
table = lookup_ops.DenseHashTable(
    dtypes.string,
    dtypes.float32,
    default_value=default_value,
    empty_key="",
    deleted_key="$",
    experimental_is_anonymous=is_anonymous)
self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(4, self.evaluate(table.size()))

remove_string = constant_op.constant(["b", "e"])
self.evaluate(table.remove(remove_string))
self.assertAllEqual(3, self.evaluate(table.size()))

input_string = constant_op.constant(["a", "b", "d", "e"], dtypes.string)
output = table.lookup(input_string)
self.assertAllEqual([4], output.get_shape())

result = self.evaluate(output)
self.assertAllClose([0, -1.5, 3.3, -1.5], result)
