# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
colocation_dict = {}
summary = error_interpolation._compute_colocation_summary_from_dict(
    "node_name", colocation_dict, prefix="  ")
self.assertIn("node_name", summary)
self.assertIn("No node-device colocations", summary)
