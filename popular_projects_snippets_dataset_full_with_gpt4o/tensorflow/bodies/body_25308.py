# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("0B", cli_shared.bytes_to_readable_str(0, include_b=True))
self.assertEqual(
    "1.00kB", cli_shared.bytes_to_readable_str(
        1024, include_b=True))
self.assertEqual(
    "1.00MB", cli_shared.bytes_to_readable_str(
        1024**2, include_b=True))
self.assertEqual(
    "1.00GB", cli_shared.bytes_to_readable_str(
        1024**3, include_b=True))
