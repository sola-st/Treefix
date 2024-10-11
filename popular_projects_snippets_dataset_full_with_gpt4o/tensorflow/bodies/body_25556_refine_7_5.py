import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=[]) # pragma: no cover
self.assertRaisesRegex = unittest.TestCase().assertRaisesRegex # pragma: no cover
command_parser = Mock(spec=['parse_time_interval']) # pragma: no cover

import unittest # pragma: no cover

class MockCommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        pattern_valid = re.compile(r'^\[.*\]|\(.*\)|<.*|>.*$') # pragma: no cover
        pattern_two_values = re.compile(r'^\[.*\]$|^\(.*\)$') # pragma: no cover
        match_valid = pattern_valid.match(interval) # pragma: no cover
        match_two_values = pattern_two_values.match(interval) # pragma: no cover
        if not match_valid: # pragma: no cover
            raise ValueError(f"Invalid interval format: {interval}. Valid formats are: \[min, max\], \(min, max\), <max, >min") # pragma: no cover
        if not match_two_values and len(interval.split(',')) != 2: # pragma: no cover
            raise ValueError(f"Incorrect interval format: {interval}. Interval should specify two values: \[min, max\] or \(min, max\)") # pragma: no cover
        min_val, max_val = interval.strip('[]()').split(', ') # pragma: no cover
        if min_val >= max_val: # pragma: no cover
            raise ValueError(f"Invalid interval {interval}. Start must be before end of interval.") # pragma: no cover
 # pragma: no cover
command_parser = MockCommandParser() # pragma: no cover
 # pragma: no cover
class MockTest(unittest.TestCase): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = type("Mock", (MockTest,), {})() # pragma: no cover

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
