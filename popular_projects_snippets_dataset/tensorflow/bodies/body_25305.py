# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("1.00k", cli_shared.bytes_to_readable_str(1024))
self.assertEqual("2.40k", cli_shared.bytes_to_readable_str(int(1024 * 2.4)))
self.assertEqual("1023.00k", cli_shared.bytes_to_readable_str(1024 * 1023))
