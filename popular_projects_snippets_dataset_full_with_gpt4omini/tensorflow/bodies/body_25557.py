# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
self.assertEqual(
    command_parser.Interval(1024, True, 2048, True),
    command_parser.parse_memory_interval("[1k, 2k]"))
self.assertEqual(
    command_parser.Interval(1024, False, 2048, False),
    command_parser.parse_memory_interval("(1kB, 2kB)"))
self.assertEqual(
    command_parser.Interval(1024, False, 2048, True),
    command_parser.parse_memory_interval("(1k, 2k]"))
self.assertEqual(
    command_parser.Interval(1024, True, 2048, False),
    command_parser.parse_memory_interval("[1k, 2k)"))
self.assertEqual(
    command_parser.Interval(0, False, 2048, True),
    command_parser.parse_memory_interval("<=2k"))
self.assertEqual(
    command_parser.Interval(11, True, float("inf"), False),
    command_parser.parse_memory_interval(">=11"))
self.assertEqual(
    command_parser.Interval(0, False, 2048, False),
    command_parser.parse_memory_interval("<2k"))
self.assertEqual(
    command_parser.Interval(11, False, float("inf"), False),
    command_parser.parse_memory_interval(">11"))
