# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(0, command_parser.parse_readable_size_str("0GB"))
self.assertEqual(1024**4, command_parser.parse_readable_size_str("1024 GB"))
self.assertEqual(1024**4 * 2,
                 command_parser.parse_readable_size_str("2048G"))
self.assertEqual(1024**4 * 2,
                 command_parser.parse_readable_size_str("2048GB"))
self.assertEqual(1024**3 / 4,
                 command_parser.parse_readable_size_str("0.25G"))
