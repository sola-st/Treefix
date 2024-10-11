# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "pt foo[1, 2, :]"
self.assertEqual(["pt", "foo[1, 2, :]"],
                 command_parser.parse_command(command))
command = "pt  foo[1, 2, :]   -a"
self.assertEqual(["pt", "foo[1, 2, :]", "-a"],
                 command_parser.parse_command(command))

command = "inject_value foo [1, 2,:] 0"
self.assertEqual(["inject_value", "foo", "[1, 2,:]", "0"],
                 command_parser.parse_command(command))
