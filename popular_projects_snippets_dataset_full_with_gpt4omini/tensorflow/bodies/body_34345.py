# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant(1.0)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Trying to lookup non-existent key. *"):
    l = map_ops.tensor_map_lookup(m, k, dtypes.float32)
    self.evaluate(l)
