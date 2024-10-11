# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
"""V1 had many different names for ops; check to make sure they rename."""
self.CheckConversion(EMPTY_TEST_SCHEMA_V1, EMPTY_TEST_SCHEMA_V3)
self.CheckConversion(FULL_TEST_SCHEMA_V1, FULL_TEST_SCHEMA_V3)
