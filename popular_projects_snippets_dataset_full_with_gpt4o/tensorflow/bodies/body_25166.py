# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Tear down temporary dump directory.
file_io.delete_recursively(cls._dump_root)
file_io.delete_recursively(cls._dump_root_for_unique)
