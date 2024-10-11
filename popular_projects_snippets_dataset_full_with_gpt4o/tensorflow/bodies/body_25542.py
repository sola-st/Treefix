# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
with self.assertRaises(SyntaxError):
    command_parser.parse_ranges("[[1,2]")

with self.assertRaisesRegex(ValueError,
                            "Incorrect number of elements in range"):
    command_parser.parse_ranges("[1,2,3]")

with self.assertRaisesRegex(ValueError,
                            "Incorrect number of elements in range"):
    command_parser.parse_ranges("[inf]")

with self.assertRaisesRegex(ValueError,
                            "Incorrect type in the 1st element of range"):
    command_parser.parse_ranges("[1j, 1]")

with self.assertRaisesRegex(ValueError,
                            "Incorrect type in the 2nd element of range"):
    command_parser.parse_ranges("[1, 1j]")
