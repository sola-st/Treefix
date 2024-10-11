# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertAllClose([[-0.1, 0.2], [10.0, 12.0]],
                    command_parser.parse_ranges("[[-0.1, 0.2], [10,  12]]"))
self.assertAllClose(
    [[-self.INF_VALUE, -1.0], [1.0, self.INF_VALUE]],
    command_parser.parse_ranges("[[-inf, -1.0],[1.0, inf]]"))
