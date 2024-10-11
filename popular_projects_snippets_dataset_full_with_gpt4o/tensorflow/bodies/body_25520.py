# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
command = "inject_value foo \"np.zeros([100, 500])\""
self.assertEqual(["inject_value", "foo", "np.zeros([100, 500])"],
                 command_parser.parse_command(command))
# The pair of double quotes should have been stripped.

command = "inject_value foo 'np.zeros([100, 500])'"
self.assertEqual(["inject_value", "foo", "np.zeros([100, 500])"],
                 command_parser.parse_command(command))
# The pair of single quotes should have been stripped.

command = "\"command prefix with spaces\" arg1"
self.assertEqual(["command prefix with spaces", "arg1"],
                 command_parser.parse_command(command))
