# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
enter = gen_control_flow_ops.enter(1, frame_name="name").op
self.assertTrue(control_flow_util.IsLoopEnter(enter))
self.assertFalse(control_flow_util.IsLoopConstantEnter(enter))

ref_enter = gen_control_flow_ops.ref_enter(test_ops.ref_output(),
                                           frame_name="name").op
self.assertTrue(control_flow_util.IsLoopEnter(ref_enter))
self.assertFalse(control_flow_util.IsLoopConstantEnter(ref_enter))

const_enter = gen_control_flow_ops.enter(1, frame_name="name",
                                         is_constant=True).op
self.assertTrue(control_flow_util.IsLoopEnter(const_enter))
self.assertTrue(control_flow_util.IsLoopConstantEnter(const_enter))

self.assertFalse(control_flow_util.IsLoopEnter(test_ops.int_output().op))
