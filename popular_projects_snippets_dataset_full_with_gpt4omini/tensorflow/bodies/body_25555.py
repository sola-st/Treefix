# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(ValueError, "Invalid first item in interval:"):
    command_parser.parse_time_interval("[wms, 10ms]")
with self.assertRaisesRegex(ValueError, "Invalid second item in interval:"):
    command_parser.parse_time_interval("[ 0ms, _ms]")
with self.assertRaisesRegex(ValueError, "Invalid first item in interval:"):
    command_parser.parse_time_interval("(xms, _ms]")
with self.assertRaisesRegex(ValueError, "Invalid first item in interval:"):
    command_parser.parse_time_interval("((3ms, _ms)")
