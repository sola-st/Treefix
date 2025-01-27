# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_disable_test.py
self.assertTrue(tf2.enabled())
self.assertFalse(control_flow_util.ENABLE_CONTROL_FLOW_V2)
