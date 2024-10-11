# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(0, command_parser.parse_readable_size_str("0MB"))
self.assertEqual(1024**3, command_parser.parse_readable_size_str("1024 MB"))
self.assertEqual(1024**3 * 2,
                 command_parser.parse_readable_size_str("2048M"))
self.assertEqual(1024**3 * 2,
                 command_parser.parse_readable_size_str("2048MB"))
self.assertEqual(1024**2 / 4,
                 command_parser.parse_readable_size_str("0.25M"))
