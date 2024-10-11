# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t1 = control_flow_ops.cond(
    math_ops.equal(list_ops.tensor_list_length(t1), 0),
    lambda: list_ops.empty_tensor_list(m.shape, m.dtype), lambda: t1)

t1 = list_ops.tensor_list_push_back(t1, m * i)
i += 1.0
exit((i, m, t1))
