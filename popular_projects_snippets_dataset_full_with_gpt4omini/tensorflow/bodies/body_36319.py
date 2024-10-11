# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
switch_false, _ = control_flow_ops.switch(1, True)
switch = switch_false.op
self.assertTrue(control_flow_util.IsSwitch(switch))

ref_switch_false, _ = control_flow_ops.ref_switch(test_ops.ref_output(),
                                                  True)
ref_switch = ref_switch_false.op
self.assertTrue(control_flow_util.IsSwitch(ref_switch))

self.assertFalse(control_flow_util.IsSwitch(test_ops.int_output().op))
