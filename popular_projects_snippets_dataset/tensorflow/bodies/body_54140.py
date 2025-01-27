# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
st = sparse_tensor.SparseTensor(indices, values, dense_shape)
tensor_list = st_spec._to_tensor_list(st)
st_reconstructed = st_spec._from_tensor_list(tensor_list)
self.assertAllEqual(st.indices, st_reconstructed.indices)
self.assertAllEqual(st.values, st_reconstructed.values)
self.assertAllEqual(st.dense_shape, st_reconstructed.dense_shape)
