# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(
    ValueError,
    r"Invalid interval \[5k, 3k\]. Start of interval must be less than or "
    "equal to end of interval."):
    command_parser.parse_memory_interval("[5k, 3k]")
