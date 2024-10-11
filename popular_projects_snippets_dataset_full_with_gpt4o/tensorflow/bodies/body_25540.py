# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertAllClose([[-0.1, 0.2]],
                    command_parser.parse_ranges("[-0.1, 0.2]"))
self.assertAllClose([[-0.1, self.INF_VALUE]],
                    command_parser.parse_ranges("[-0.1, inf]"))
self.assertAllClose([[-self.INF_VALUE, self.INF_VALUE]],
                    command_parser.parse_ranges("[-inf, inf]"))
