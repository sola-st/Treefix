# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    handle = list_ops.tensor_list_reserve([2], 10, dtypes.int32)
    handle = list_ops.tensor_list_scatter(
        [[1, i], [i + 1, 2]],
        [i, i + 5], input_handle=handle)
    exit(list_ops.tensor_list_stack(handle, dtypes.int32))

self._test_loop_fn(loop_fn, 5)
