# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(ValueError, r".*float.*2us.*"):
    command_parser.parse_readable_time_str("2uss")

with self.assertRaisesRegex(ValueError, r".*float.*2m.*"):
    command_parser.parse_readable_time_str("2m")

with self.assertRaisesRegex(
    ValueError, r"Invalid time -1. Time value must be positive."):
    command_parser.parse_readable_time_str("-1s")
