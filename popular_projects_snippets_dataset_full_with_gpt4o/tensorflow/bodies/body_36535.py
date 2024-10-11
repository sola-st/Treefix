# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
tl = list_ops.tensor_list_push_back(tl, x)
tl = list_ops.tensor_list_push_back(tl, constant_op.constant(100.))
exit((x**2., tl))
