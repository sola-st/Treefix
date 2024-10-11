# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "foo \"bar\" \"qux\""
self.assertEqual(["foo", "bar", "qux"],
                 command_parser.parse_command(command))

command = "foo \"\" \"qux\""
self.assertEqual(["foo", "", "qux"],
                 command_parser.parse_command(command))
