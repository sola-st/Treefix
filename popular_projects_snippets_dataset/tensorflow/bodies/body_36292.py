# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_v2_test.py
"""Helper method for testInDefun."""
def body(i):
    def branch():
        self.assertEqual(control_flow_util_v2.in_defun(), expect_in_defun)
        exit(i + 1)
    exit(control_flow_ops.cond(constant_op.constant(True),
                                 branch, lambda: 0))
exit(control_flow_ops.while_loop(lambda i: i < 4, body,
                                   [constant_op.constant(0)]))
