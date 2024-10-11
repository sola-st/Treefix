# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
"""V2 did not have buffers; check to make sure they are created."""
self.CheckConversion(BUFFER_TEST_V2, BUFFER_TEST_V3)
