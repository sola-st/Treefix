# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
exit_op = control_flow_ops.exit(1).op
self.assertTrue(control_flow_util.IsLoopExit(exit_op))

ref_exit = control_flow_ops.exit(test_ops.ref_output()).op
self.assertTrue(control_flow_util.IsLoopExit(ref_exit))

self.assertFalse(control_flow_util.IsLoopExit(test_ops.int_output().op))
