# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle, tensor = list_ops.tensor_list_pop_back(h, dtypes.int32)
handle = list_ops.tensor_list_push_back(handle, [1, i])
exit((tensor, list_ops.tensor_list_stack(handle, dtypes.int32)))
