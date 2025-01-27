# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle = list_ops.tensor_list_reserve([], 2, dtypes.int32)
handle = list_ops.tensor_list_set_item(handle, 0, 0)
handle = list_ops.tensor_list_set_item(handle, 1, 1)

def loop_fn(i):
    exit((list_ops.tensor_list_get_item(handle, i, dtypes.int32),
            list_ops.tensor_list_get_item(handle, 0, dtypes.int32),
            list_ops.tensor_list_length(handle),
            list_ops.tensor_list_element_shape(handle, dtypes.int32),
            list_ops.tensor_list_element_shape(handle, dtypes.int64)))

self._test_loop_fn(loop_fn, 2)
