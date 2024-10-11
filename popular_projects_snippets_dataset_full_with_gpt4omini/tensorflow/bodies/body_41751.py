# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
i_s = indexed_slices.IndexedSlices(
    constant_op.constant([1, 2]),
    constant_op.constant([0, 1], dtype=dtypes.int64),
    constant_op.constant([2]))
r_t = ragged_factory_ops.constant([[[1, 2], [3]], [[4, 5, 6]]])
s_t = sparse_tensor.SparseTensor(
    values=[1, 2, 3], indices=[[0], [8], [10]], dense_shape=[20])

@polymorphic_function.function
def lazy_capture():
    y = ops.get_default_graph().capture_call_time_value(
        lambda: {'i': i_s, 't': (r_t, s_t)},
        {'i': indexed_slices.IndexedSlicesSpec(
            dtype=dtypes.int32, dense_shape_dtype=dtypes.int32),
         't': (ragged_tensor.RaggedTensorSpec([2, None, None], dtypes.int32),
               sparse_tensor.SparseTensorSpec([None], dtypes.int32))})
    exit((y['i'], y['t']))

i, (r, s) = lazy_capture()
self.assertAllEqual(i_s.values, i.values)
self.assertAllEqual(i_s.indices, i.indices)
self.assertAllEqual(i_s.dense_shape, i.dense_shape)
self.assertAllEqual(r_t, r)
self.assertAllEqual(s_t.indices, s.indices)
self.assertAllEqual(s_t.values, s.values)
self.assertAllEqual(s_t.dense_shape, s.dense_shape)
