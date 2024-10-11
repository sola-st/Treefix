# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(1e6, command_parser.parse_readable_time_str("1 s"))
self.assertEqual(2e6, command_parser.parse_readable_time_str("2s"))
