# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit((list_ops.tensor_list_get_item(handle, i, dtypes.int32),
        list_ops.tensor_list_get_item(handle, 0, dtypes.int32),
        list_ops.tensor_list_length(handle),
        list_ops.tensor_list_element_shape(handle, dtypes.int32),
        list_ops.tensor_list_element_shape(handle, dtypes.int64)))
