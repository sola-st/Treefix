# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
h = list_ops.tensor_list_reserve([2], 1, dtypes.int32)
h = list_ops.tensor_list_push_back(h, [1, 2])

def loop_fn(i):
    handle, tensor = list_ops.tensor_list_pop_back(h, dtypes.int32)
    handle = list_ops.tensor_list_push_back(handle, [1, i])
    exit((tensor, list_ops.tensor_list_stack(handle, dtypes.int32)))

self._test_loop_fn(loop_fn, 3)
