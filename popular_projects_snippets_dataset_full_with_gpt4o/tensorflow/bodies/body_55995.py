# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec_type()
self.assertEqual("", d.to_string())
d.parse_from_string("")
self.assertEqual("", d.to_string())
