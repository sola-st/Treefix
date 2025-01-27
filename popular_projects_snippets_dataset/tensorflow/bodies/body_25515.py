# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = ""
self.assertEqual([], command_parser.parse_command(command))

command = "a"
self.assertEqual(["a"], command_parser.parse_command(command))

command = "foo bar baz qux"
self.assertEqual(["foo", "bar", "baz", "qux"],
                 command_parser.parse_command(command))

command = "foo bar\tbaz\t qux"
self.assertEqual(["foo", "bar", "baz", "qux"],
                 command_parser.parse_command(command))
