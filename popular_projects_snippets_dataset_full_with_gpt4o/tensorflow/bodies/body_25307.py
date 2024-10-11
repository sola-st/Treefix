# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("1.00G", cli_shared.bytes_to_readable_str(1024**3))
self.assertEqual("2000.00G",
                 cli_shared.bytes_to_readable_str(1024**3 * 2000))
