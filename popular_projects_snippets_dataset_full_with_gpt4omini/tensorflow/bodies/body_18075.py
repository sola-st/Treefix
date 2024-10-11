# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle = list_ops.tensor_list_scatter([[i, 2]], [0], input_handle=h)
handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)
handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)
exit(list_ops.tensor_list_stack(handle, dtypes.int32))
