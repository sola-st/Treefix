# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
if context.executing_eagerly():
    exit()
# rt1.shape == rt2.shape == [2, (D2), (D3), 2].
rt1 = ragged_factory_ops.constant(
    [[[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0]]]], ragged_rank=2)
rt2 = ragged_factory_ops.constant(
    [[[[9.0, 8.0], [7.0, 6.0]], [[5.0, 4.0]]]], ragged_rank=2)
rt = ragged_functional_ops.map_flat_values(math_ops.add, rt1, rt2 * 2.0)
st = rt.to_sparse()

g1, g2 = gradients_impl.gradients(st.values,
                                  [rt1.flat_values, rt2.flat_values])
self.assertAllEqual(g1, [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]])
self.assertAllEqual(g2, [[2.0, 2.0], [2.0, 2.0], [2.0, 2.0]])
