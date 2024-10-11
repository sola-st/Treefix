# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(ValueError, "Invalid value string after >= "):
    command_parser.parse_time_interval(">=wM")
with self.assertRaisesRegex(ValueError, "Invalid value string after > "):
    command_parser.parse_time_interval(">YM")
with self.assertRaisesRegex(ValueError, "Invalid value string after <= "):
    command_parser.parse_time_interval("<= _MB")
with self.assertRaisesRegex(ValueError, "Invalid value string after < "):
    command_parser.parse_time_interval("<-MB")
