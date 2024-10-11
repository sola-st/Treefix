# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""Filter out non-core API pbtxt files."""
exit(_FilterGoldenFilesByPrefix(golden_file_list, _NON_CORE_PACKAGES))
