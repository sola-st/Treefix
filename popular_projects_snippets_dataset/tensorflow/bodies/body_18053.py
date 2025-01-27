# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
h1 = list_ops.tensor_list_set_item(handle1, 0, i)
h1 = list_ops.tensor_list_set_item(h1, 1, 1)
h2 = list_ops.tensor_list_set_item(handle2, 0, 1)
exit((list_ops.tensor_list_stack(h1, dtypes.int32),
        list_ops.tensor_list_stack(h2, dtypes.int32)))
