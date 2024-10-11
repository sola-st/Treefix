import unittest # pragma: no cover

class CommandParser: # pragma: no cover
    def parse_time_interval(self, interval): # pragma: no cover
        if interval == '[10us, 1ms': # pragma: no cover
            raise ValueError('Invalid interval format: [10us, 1ms. Valid formats are: [min, max], (min, max), <max, >min') # pragma: no cover
        elif interval == '[10us, 1ms, 2ms]': # pragma: no cover
            raise ValueError('Incorrect interval format: [10us, 1ms, 2ms]. Interval should specify two values: [min, max] or (min, max)') # pragma: no cover
        elif interval == '[1s, 1ms]': # pragma: no cover
            raise ValueError('Invalid interval [1s, 1ms]. Start must be before end of interval.') # pragma: no cover
 # pragma: no cover
command_parser = CommandParser() # pragma: no cover
 # pragma: no cover
class MockSelf(unittest.TestCase): # pragma: no cover
    pass # pragma: no cover
self = MockSelf() # pragma: no cover

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
