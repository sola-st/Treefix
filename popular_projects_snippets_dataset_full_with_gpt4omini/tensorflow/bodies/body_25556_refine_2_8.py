import unittest # pragma: no cover
class CommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        # Mock implementation for parsing time intervals # pragma: no cover
        if not isinstance(interval, str): # pragma: no cover
            raise ValueError('Invalid interval format.') # pragma: no cover
        if interval.count(',') != 1: # pragma: no cover
            raise ValueError('Incorrect interval format.') # pragma: no cover
        # Add additional parsing logic as necessary # pragma: no cover

self = unittest.TestCase() # pragma: no cover
command_parser = CommandParser() # pragma: no cover

import unittest # pragma: no cover
class CommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        if not isinstance(interval, str): # pragma: no cover
            raise ValueError('Invalid interval format: {}'.format(interval)) # pragma: no cover
        interval = interval.strip() # pragma: no cover
        if interval[-1] != ']': # pragma: no cover
            raise ValueError('Invalid interval format: {}'.format(interval)) # pragma: no cover
        parts = interval[1:-1].split(',') # pragma: no cover
        if len(parts) != 2: # pragma: no cover
            raise ValueError('Incorrect interval format: {}'.format(interval)) # pragma: no cover
        # Further checks can be added here # pragma: no cover

self = unittest.TestCase() # pragma: no cover
command_parser = CommandParser() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser_test.py
from l3.Runtime import _l_
with self.assertRaisesRegex(
    ValueError, r"Invalid interval format: \[10us, 1ms. Valid formats are: "
    r"\[min, max\], \(min, max\), <max, >min"):
    _l_(10010)

    command_parser.parse_time_interval("[10us, 1ms")
    _l_(10009)
with self.assertRaisesRegex(
    ValueError,
    r"Incorrect interval format: \[10us, 1ms, 2ms\]. Interval should "
    r"specify two values: \[min, max\] or \(min, max\)"):
    _l_(10012)

    command_parser.parse_time_interval("[10us, 1ms, 2ms]")
    _l_(10011)
with self.assertRaisesRegex(
    ValueError,
    r"Invalid interval \[1s, 1ms\]. Start must be before end of interval."):
    _l_(10014)

    command_parser.parse_time_interval("[1s, 1ms]")
    _l_(10013)
