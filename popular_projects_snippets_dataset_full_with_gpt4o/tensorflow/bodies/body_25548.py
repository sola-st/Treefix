# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(0, command_parser.parse_readable_time_str("0"))
self.assertEqual(100, command_parser.parse_readable_time_str("100 "))
self.assertEqual(25, command_parser.parse_readable_time_str(" 25 "))
