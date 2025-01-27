# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(0, command_parser.parse_readable_size_str("0"))
self.assertEqual(1024, command_parser.parse_readable_size_str("1024 "))
self.assertEqual(2000, command_parser.parse_readable_size_str(" 2000 "))
