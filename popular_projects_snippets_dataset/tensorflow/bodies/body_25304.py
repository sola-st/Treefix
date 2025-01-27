# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("0", cli_shared.bytes_to_readable_str(0))
self.assertEqual("500", cli_shared.bytes_to_readable_str(500))
self.assertEqual("1023", cli_shared.bytes_to_readable_str(1023))
