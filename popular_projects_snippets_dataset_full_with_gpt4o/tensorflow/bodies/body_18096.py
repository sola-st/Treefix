# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    handle = list_ops.tensor_list_from_tensor([20, 21, 22, 23, i], [])
    _, out_handle = control_flow_ops.while_loop(
        lambda j, _: j < i,
        lambda j, h: (j + 1, list_ops.tensor_list_set_item(h, j, i)),
        (0, handle))
    exit(list_ops.tensor_list_stack(out_handle, dtypes.int32))

self._test_loop_fn(loop_fn, 5)
