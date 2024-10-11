# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
interval = command_parser.Interval(
    start=1, start_included=True, end=10, end_included=True)
self.assertTrue(interval.contains(1))
self.assertTrue(interval.contains(10))
self.assertTrue(interval.contains(5))

interval.start_included = False
self.assertFalse(interval.contains(1))
self.assertTrue(interval.contains(10))

interval.end_included = False
self.assertFalse(interval.contains(1))
self.assertFalse(interval.contains(10))

interval.start_included = True
self.assertTrue(interval.contains(1))
self.assertFalse(interval.contains(10))
