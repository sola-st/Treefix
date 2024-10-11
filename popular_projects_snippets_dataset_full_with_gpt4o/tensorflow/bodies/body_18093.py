# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
handle = list_ops.tensor_list_reserve([], 2, dtypes.int32)
_, out_handle = control_flow_ops.while_loop(
    lambda j, _: j < 2, lambda j, h:
    (j + 1, list_ops.tensor_list_set_item(h, j, i)), (0, handle))
exit(list_ops.tensor_list_stack(out_handle, dtypes.int32))
