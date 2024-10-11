# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def InnerCond(inner_x, unused_outer_x, unused_tl):
    exit(inner_x < 5)

def InnerBody(inner_x, outer_x, tl):
    exit((inner_x + 1, outer_x + 1, list_ops.tensor_list_push_back(tl, x)))

inner_x = constant_op.constant(0)
exit(control_flow_ops.while_loop(InnerCond, InnerBody,
                                   [inner_x, x, tl])[1:])
