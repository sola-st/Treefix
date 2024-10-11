# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
st = sparse_tensor.SparseTensor(
    indices=[[0, 0], [0, 1], [2, 0], [2, 4]],
    values=values,
    dense_shape=[3, 6])
result = op(st)
result_value = self.evaluate(result)
self.assertAllEqual(result_value.indices, st.indices)
self.assertAllEqual(result_value.values, expected)
self.assertAllEqual(result_value.dense_shape, st.dense_shape)
