# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
kwargs = kwargs or {}
result = ragged_functional_ops.map_flat_values(op, *args, **kwargs)
self.assertAllEqual(result, expected)
