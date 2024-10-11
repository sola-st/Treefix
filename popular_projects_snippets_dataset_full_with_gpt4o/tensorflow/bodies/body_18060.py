# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    h1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)
    h1 = list_ops.tensor_list_set_item(h1, 0, i)
    h1 = list_ops.tensor_list_set_item(h1, 1, 1)
    h2 = list_ops.tensor_list_reserve([], 2, dtypes.int32)
    h2 = list_ops.tensor_list_set_item(h2, 0, 1)
    exit((list_ops.tensor_list_stack(h1, dtypes.int32),
            list_ops.tensor_list_stack(h2, dtypes.int32)))

self._test_loop_fn(loop_fn, 3)
