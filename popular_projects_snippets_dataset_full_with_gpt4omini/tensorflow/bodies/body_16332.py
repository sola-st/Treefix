# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_toggles_test.py
self.assertIsNone(
    control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE)
control_flow_v2_toggles.output_all_intermediates(True)
self.assertTrue(
    control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE)
control_flow_v2_toggles.output_all_intermediates(False)
self.assertFalse(
    control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE)
control_flow_v2_toggles.output_all_intermediates(None)
self.assertIsNone(
    control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE)
