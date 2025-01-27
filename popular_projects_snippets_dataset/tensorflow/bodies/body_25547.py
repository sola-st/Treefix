# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(
    ValueError, "Failed to parsed human-readable byte size str: \"0foo\""):
    command_parser.parse_readable_size_str("0foo")

with self.assertRaisesRegex(
    ValueError, "Failed to parsed human-readable byte size str: \"2E\""):
    command_parser.parse_readable_size_str("2EB")
