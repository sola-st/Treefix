import unittest # pragma: no cover
import re # pragma: no cover

self = type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover
command_parser = type('Mock', (object,), {'parse_time_interval': lambda x: None})() # pragma: no cover

import unittest # pragma: no cover
import re # pragma: no cover

self = type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover
def parse_time_interval(interval): # pragma: no cover
    valid_patterns = [ # pragma: no cover
        re.compile(r'^\[\d+us, \d+ms\]$'), # pragma: no cover
        re.compile(r'^\(\d+us, \d+ms\)$'), # pragma: no cover
        re.compile(r'^<\d+ms>$'), # pragma: no cover
        re.compile(r'^>\d+us>$'), # pragma: no cover
    ] # pragma: no cover
    if not any(p.match(interval) for p in valid_patterns): # pragma: no cover
        raise ValueError(f'Invalid interval format: {interval}. Valid formats are: \[min, max\], \(min, max\), <max, >min') # pragma: no cover
command_parser = type('Mock', (object,), {'parse_time_interval': parse_time_interval})() # pragma: no cover

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
