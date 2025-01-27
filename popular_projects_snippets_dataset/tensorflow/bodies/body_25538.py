# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaisesRegex(
    ValueError, r"invalid literal for int\(\) with base 10: 'a'"):
    self.assertEqual([0], command_parser.parse_indices("0,a"))

with self.assertRaisesRegex(
    ValueError, r"invalid literal for int\(\) with base 10: '2\]'"):
    self.assertEqual([0], command_parser.parse_indices("1, 2]"))

with self.assertRaisesRegex(
    ValueError, r"invalid literal for int\(\) with base 10: ''"):
    self.assertEqual([0], command_parser.parse_indices("3, 4,"))
