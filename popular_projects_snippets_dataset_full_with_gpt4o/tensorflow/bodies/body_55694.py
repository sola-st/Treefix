# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
assignments = []
assignments.append(
    traceable_stack.TraceableObject(
        "/cpu:0", filename="hope.py", lineno=24))
assignments.append(
    traceable_stack.TraceableObject(
        "/gpu:2", filename="please.py", lineno=42))

summary = error_interpolation._compute_device_summary_from_list(
    "nodename", assignments, prefix="  ")

self.assertIn("nodename", summary)
self.assertIn("tf.device(/cpu:0)", summary)
self.assertIn("<hope.py:24>", summary)
self.assertIn("tf.device(/gpu:2)", summary)
self.assertIn("<please.py:42>", summary)
