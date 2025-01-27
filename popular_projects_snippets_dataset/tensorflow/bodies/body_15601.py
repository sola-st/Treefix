# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
# x and y are equal, except that x has uniform_row_length and y does not.
x = ragged_tensor.RaggedTensor.from_uniform_row_length(
    ragged_factory_ops.constant([[1, 2], [3]]), uniform_row_length=2)
y = ragged_factory_ops.constant([[[1, 2], [3]]])

a = ragged_functional_ops.map_flat_values(math_ops.add, x, y)
self.assertAllEqual(x.uniform_row_length, a.uniform_row_length)

b = ragged_functional_ops.map_flat_values(math_ops.add, y, x)
self.assertAllEqual(x.uniform_row_length, b.uniform_row_length)

c = ragged_functional_ops.map_flat_values(math_ops.add_n, [x, x])
self.assertAllEqual(x.uniform_row_length, c.uniform_row_length)

d = ragged_functional_ops.map_flat_values(math_ops.add_n, [y, x, y])
self.assertAllEqual(x.uniform_row_length, d.uniform_row_length)
