# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    handle = list_ops.tensor_list_reserve([2], 2, dtypes.int32)
    handle = list_ops.tensor_list_push_back(handle, [i, 2])
    handle = list_ops.tensor_list_push_back(handle, [1, 2])
    exit(list_ops.tensor_list_stack(handle, dtypes.int32))

self._test_loop_fn(loop_fn, 3)
