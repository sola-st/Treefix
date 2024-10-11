# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(
    command_parser.Interval(10, True, 1e3, True),
    command_parser.parse_time_interval("[10us, 1ms]"))
self.assertEqual(
    command_parser.Interval(10, False, 1e3, False),
    command_parser.parse_time_interval("(10us, 1ms)"))
self.assertEqual(
    command_parser.Interval(10, False, 1e3, True),
    command_parser.parse_time_interval("(10us, 1ms]"))
self.assertEqual(
    command_parser.Interval(10, True, 1e3, False),
    command_parser.parse_time_interval("[10us, 1ms)"))
self.assertEqual(
    command_parser.Interval(0, False, 1e3, True),
    command_parser.parse_time_interval("<=1ms"))
self.assertEqual(
    command_parser.Interval(1e3, True, float("inf"), False),
    command_parser.parse_time_interval(">=1ms"))
self.assertEqual(
    command_parser.Interval(0, False, 1e3, False),
    command_parser.parse_time_interval("<1ms"))
self.assertEqual(
    command_parser.Interval(1e3, False, float("inf"), False),
    command_parser.parse_time_interval(">1ms"))
