# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
"""Verify the DebugInfo is valid."""
file_names = set()
for file_path in debug_info.files:
    file_names.add(os.path.basename(file_path))
# To make the test independent on how the nodes are created, we only assert
# the name of this test file.
self.assertIn('lite_v2_test.py', file_names)
self.assertNotIn('lite_test.py', file_names)
