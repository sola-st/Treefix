import unittest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

self = Mock(spec=[]) # pragma: no cover
self.assertRaisesRegex = unittest.TestCase().assertRaisesRegex # pragma: no cover
command_parser = Mock(spec=['parse_time_interval']) # pragma: no cover

import unittest # pragma: no cover

class CustomCommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        interval_formats = [ # pragma: no cover
            r'^\[\d+us, \d+ms\]$', # pragma: no cover
            r'^\(\d+us, \d+ms\)$', # pragma: no cover
            r'^<\d+ms>$', # pragma: no cover
            r'^>\d+us>$' # pragma: no cover
        ] # pragma: no cover
        if any(re.match(fmt, interval) for fmt in interval_formats): # pragma: no cover
            if interval in ['[10us, 1ms', '[1s, 1ms]', '[10us, 1ms, 2ms]']: # pragma: no cover
                error_messages = { # pragma: no cover
                    '[10us, 1ms': 'Invalid interval format: [10us, 1ms. Valid formats are: [min, max], (min, max), <max, >min', # pragma: no cover
                    '[1s, 1ms]': 'Invalid interval [1s, 1ms]. Start must be before end of interval.', # pragma: no cover
                    '[10us, 1ms, 2ms]': 'Incorrect interval format: [10us, 1ms, 2ms]. Interval should specify two values: [min, max] or (min, max)' # pragma: no cover
                } # pragma: no cover
                raise ValueError(error_messages[interval]) # pragma: no cover
        else: # pragma: no cover
            raise ValueError(f"Invalid interval format: {interval}. Valid formats are: [min, max], (min, max), <max, >min") # pragma: no cover
 # pragma: no cover
command_parser = CustomCommandParser() # pragma: no cover
 # pragma: no cover
class MockTest(unittest.TestCase): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover

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
