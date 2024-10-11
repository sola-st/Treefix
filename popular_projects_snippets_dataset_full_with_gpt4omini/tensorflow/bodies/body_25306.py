# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("1.00M", cli_shared.bytes_to_readable_str(1024**2))
self.assertEqual("2.40M",
                 cli_shared.bytes_to_readable_str(int(1024**2 * 2.4)))
self.assertEqual("1023.00M",
                 cli_shared.bytes_to_readable_str(1024**2 * 1023))
