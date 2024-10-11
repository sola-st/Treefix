# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
# There is an accumulator in the loop already so we should not add
# another.
tl = list_ops.tensor_list_push_back(tl, x)
exit((x**2., tl))
