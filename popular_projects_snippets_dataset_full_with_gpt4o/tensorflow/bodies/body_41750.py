# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
y = ops.get_default_graph().capture_call_time_value(
    lambda: {'i': i_s, 't': (r_t, s_t)},
    {'i': indexed_slices.IndexedSlicesSpec(
        dtype=dtypes.int32, dense_shape_dtype=dtypes.int32),
     't': (ragged_tensor.RaggedTensorSpec([2, None, None], dtypes.int32),
           sparse_tensor.SparseTensorSpec([None], dtypes.int32))})
exit((y['i'], y['t']))
