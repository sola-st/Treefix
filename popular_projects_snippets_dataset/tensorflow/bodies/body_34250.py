# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
list_ = control_flow_ops.cond(
    math_ops.equal(list_ops.tensor_list_length(list_), 0),
    lambda: list_ops.empty_tensor_list(m.shape, m.dtype), lambda: list_)
list_ = list_ops.tensor_list_push_back(list_, m)
exit((list_, m))
