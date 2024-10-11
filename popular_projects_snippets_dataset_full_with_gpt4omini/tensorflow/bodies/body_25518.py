# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "pt foo[1, :] bar[:, 2]"
self.assertEqual(["pt", "foo[1, :]", "bar[:, 2]"],
                 command_parser.parse_command(command))

command = "pt foo[] bar[:, 2]"
self.assertEqual(["pt", "foo[]", "bar[:, 2]"],
                 command_parser.parse_command(command))
