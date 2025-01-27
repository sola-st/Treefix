# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(0, command_parser.parse_readable_size_str("0kB"))
self.assertEqual(1024**2, command_parser.parse_readable_size_str("1024 kB"))
self.assertEqual(1024**2 * 2,
                 command_parser.parse_readable_size_str("2048k"))
self.assertEqual(1024**2 * 2,
                 command_parser.parse_readable_size_str("2048kB"))
self.assertEqual(1024 / 4, command_parser.parse_readable_size_str("0.25k"))
