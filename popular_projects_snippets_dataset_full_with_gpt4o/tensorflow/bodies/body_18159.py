# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
self._enabled = control_flow_v2_toggles.control_flow_v2_enabled()
control_flow_v2_toggles.enable_control_flow_v2()
super(WhileV2Test, self).setUp()
