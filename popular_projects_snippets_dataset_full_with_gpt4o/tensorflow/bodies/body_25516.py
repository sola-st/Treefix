# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "  foo bar baz qux   "
self.assertEqual(["foo", "bar", "baz", "qux"],
                 command_parser.parse_command(command))

command = "\nfoo bar baz qux\n"
self.assertEqual(["foo", "bar", "baz", "qux"],
                 command_parser.parse_command(command))
