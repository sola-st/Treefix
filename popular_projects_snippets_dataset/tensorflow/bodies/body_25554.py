# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(ValueError, "Invalid value string after >= "):
    command_parser.parse_time_interval(">=wms")
with self.assertRaisesRegex(ValueError, "Invalid value string after > "):
    command_parser.parse_time_interval(">Yms")
with self.assertRaisesRegex(ValueError, "Invalid value string after <= "):
    command_parser.parse_time_interval("<= _ms")
with self.assertRaisesRegex(ValueError, "Invalid value string after < "):
    command_parser.parse_time_interval("<-ms")
