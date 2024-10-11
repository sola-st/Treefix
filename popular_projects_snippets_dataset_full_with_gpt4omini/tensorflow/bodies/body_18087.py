# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle = list_ops.tensor_list_reserve([2], 2, dtypes.int32)
handle = list_ops.tensor_list_scatter([[i, 2]], [0], input_handle=handle)
handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)
exit(gen_list_ops.tensor_list_concat_v2(
    handle,
    element_dtype=dtypes.int32,
    element_shape=[2],
    leading_dims=[]))
