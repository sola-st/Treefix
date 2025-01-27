# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
l1 = list_ops.tensor_list_reserve([], 2, dtypes.int32)
l1 = list_ops.tensor_list_set_item(l1, 1, 1)

def loop_fn(i):
    l2 = list_ops.tensor_list_reserve([], 2, dtypes.int32)
    l2 = list_ops.tensor_list_set_item(l2, 1, i)
    exit(list_ops.tensor_list_stack(
        math_ops.add_n([l1, l2]), dtypes.int32))

self._test_loop_fn(loop_fn, 2)
