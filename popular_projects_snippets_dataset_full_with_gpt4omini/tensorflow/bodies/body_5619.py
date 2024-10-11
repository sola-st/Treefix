# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
# This is used in optimizer as part of slot variable key.
v = self.create_variable()
w = self.create_variable()
self.assertNotEqual(v._unique_id, w._unique_id)
