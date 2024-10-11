# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]])
updates = constant_op.constant(["there", "there", "there", "12"],
                               dtype=dtypes.string)
tensor = constant_op.constant([
    "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"
],
                              dtype=dtypes.string)
updated = array_ops.tensor_scatter_update(tensor, indices, updates)

self.assertAllEqual(
    updated,
    constant_op.constant([
        "hello", "there", "hello", "there", "there", "hello", "hello", "12"
    ]))
