# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
st = sparse_tensor.SparseTensor(indices, values, dense_shape)
actual_components = st_spec._to_components(st)
self.assertAllTensorsEqual(actual_components,
                           [indices, values, dense_shape])
st_reconstructed = st_spec._from_components(actual_components)
self.assertAllEqual(st.indices, st_reconstructed.indices)
self.assertAllEqual(st.values, st_reconstructed.values)
self.assertAllEqual(st.dense_shape, st_reconstructed.dense_shape)
