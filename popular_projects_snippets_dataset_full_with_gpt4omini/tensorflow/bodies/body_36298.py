# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with self.cached_session():
    st = sparse_tensor.SparseTensor(
        indices=[[0, 0], [0, 1], [1, 0]],
        values=constant_op.constant([0, 1, 2]),
        dense_shape=[2, 2])
    result = map_fn.map_fn(lambda x: x, st)
    self.assertAllEqual(result.indices, st.indices)
    self.assertAllEqual(result.values, st.values)
    self.assertAllEqual(result.dense_shape, st.dense_shape)
