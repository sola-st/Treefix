# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual([0], command_parser.parse_indices("0"))
self.assertEqual([0], command_parser.parse_indices(" 0 "))
self.assertEqual([-1, 2], command_parser.parse_indices("-1, 2"))
self.assertEqual([3, 4, -5], command_parser.parse_indices("3,4,-5"))
