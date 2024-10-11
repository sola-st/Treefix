# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
device_assignment_list = []
summary = error_interpolation._compute_device_summary_from_list(
    "nodename", device_assignment_list, prefix="  ")
self.assertIn("nodename", summary)
self.assertIn("No device assignments", summary)
