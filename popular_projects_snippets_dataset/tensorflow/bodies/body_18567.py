# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
if not self._enabled:
    control_flow_v2_toggles.disable_control_flow_v2()
super(WhileV2Test, self).tearDown()
