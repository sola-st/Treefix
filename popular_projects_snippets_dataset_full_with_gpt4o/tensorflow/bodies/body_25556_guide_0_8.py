import unittest # pragma: no cover
import re # pragma: no cover

class MockCommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        raise ValueError('Mock error') # pragma: no cover
 # pragma: no cover
command_parser = MockCommandParser() # pragma: no cover
 # pragma: no cover
class TestIntervals(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        self.command_parser = command_parser # pragma: no cover
 # pragma: no cover
test_case = TestIntervals() # pragma: no cover
test_case.setUp() # pragma: no cover
unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegex.__get__(test_case) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
from l3.Runtime import _l_
with self.assertRaisesRegex(
    ValueError, r"Invalid interval format: \[10us, 1ms. Valid formats are: "
    r"\[min, max\], \(min, max\), <max, >min"):
    _l_(22299)

    command_parser.parse_time_interval("[10us, 1ms")
    _l_(22298)
with self.assertRaisesRegex(
    ValueError,
    r"Incorrect interval format: \[10us, 1ms, 2ms\]. Interval should "
    r"specify two values: \[min, max\] or \(min, max\)"):
    _l_(22301)

    command_parser.parse_time_interval("[10us, 1ms, 2ms]")
    _l_(22300)
with self.assertRaisesRegex(
    ValueError,
    r"Invalid interval \[1s, 1ms\]. Start must be before end of interval."):
    _l_(22303)

    command_parser.parse_time_interval("[1s, 1ms]")
    _l_(22302)
