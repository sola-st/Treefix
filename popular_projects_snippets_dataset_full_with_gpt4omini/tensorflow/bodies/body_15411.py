# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
# Unary elementwise op
rt = ragged_tensor.RaggedTensor.from_uniform_row_length(
    ragged_factory_ops.constant([[1, 2], [3]]), uniform_row_length=2)
self.assertAllEqual(rt.uniform_row_length,
                    array_ops.zeros_like(rt).uniform_row_length)

# Unary-list elementwise op
rt = ragged_tensor.RaggedTensor.from_uniform_row_length(
    ragged_factory_ops.constant([[1, 2], [3]]), uniform_row_length=2)
self.assertAllEqual(rt.uniform_row_length,
                    math_ops.add_n([rt, rt]).uniform_row_length)
