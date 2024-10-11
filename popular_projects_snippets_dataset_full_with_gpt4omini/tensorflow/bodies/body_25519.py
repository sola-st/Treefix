# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "pt  foo[1, 2, :"
self.assertNotEqual(["pt", "foo[1, 2, :]"],
                    command_parser.parse_command(command))
