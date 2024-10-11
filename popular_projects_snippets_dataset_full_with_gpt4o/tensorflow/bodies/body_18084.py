# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle = list_ops.tensor_list_reserve([2], 2, dtypes.int32)
handle = list_ops.tensor_list_scatter([[2, 3]], [0], input_handle=handle)
handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)

def loop_fn(i):
    exit((list_ops.tensor_list_gather(handle, [0, 1], dtypes.int32),
            list_ops.tensor_list_gather(handle, [i], dtypes.int32)))

self._test_loop_fn(loop_fn, 2)
