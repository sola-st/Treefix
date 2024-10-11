import re # pragma: no cover
import unittest # pragma: no cover

class CommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        if interval.count('[') != interval.count(']') or interval.count('(') != interval.count(')'): # pragma: no cover
            raise ValueError('Invalid interval format: ' + interval + '. Valid formats are: [min, max], (min, max), <max, >min') # pragma: no cover
        interval = interval.strip('[]') # pragma: no cover
        values = interval.split(',') # pragma: no cover
        if len(values) != 2: # pragma: no cover
            raise ValueError('Incorrect interval format: ' + interval + '. Interval should specify two values: [min, max] or (min, max)') # pragma: no cover
        start, end = values[0].strip(), values[1].strip() # pragma: no cover
        if start >= end: # pragma: no cover
            raise ValueError('Invalid interval [' + start + ', ' + end + ']. Start must be before end of interval.') # pragma: no cover
 # pragma: no cover
command_parser = CommandParser() # pragma: no cover
unittest.TestCase = type('TestCase', (object,), {}) # pragma: no cover
self = unittest.TestCase() # pragma: no cover

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
