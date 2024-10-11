# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
"""A file already at version 3 should stay at version 3."""
self.CheckConversion(EMPTY_TEST_SCHEMA_V3, EMPTY_TEST_SCHEMA_V3)
self.CheckConversion(TEST_SCHEMA_V3, TEST_SCHEMA_V3)
self.CheckConversion(BUFFER_TEST_V3, BUFFER_TEST_V3)
