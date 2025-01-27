# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
resource1.assign_add(2.0)
exit((resource1 * 2, resource1.handle))
