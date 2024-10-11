import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), {'assertRaisesRegex': unittest.TestCase().assertRaisesRegex})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: x if isinstance(x, (list, tuple, set)) else (_ for _ in ()).throw(TypeError('to be iterable'))})() # pragma: no cover

import unittest # pragma: no cover

class MockSelf(unittest.TestCase): # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, callable_obj=None, *args, **kwargs): # pragma: no cover
        if callable_obj is None: # pragma: no cover
            raise ValueError('assertRaisesRegex needs a callable as an argument') # pragma: no cover
        try: # pragma: no cover
            callable_obj(*args, **kwargs) # pragma: no cover
        except expected_exception as e: # pragma: no cover
            if not self._regex_match(expected_regex, str(e)): # pragma: no cover
                raise self.failureException(f'"{expected_regex}" does not match "{str(e)}"') # pragma: no cover
        else: # pragma: no cover
            self.fail(f'{expected_exception.__name__} not raised') # pragma: no cover
 # pragma: no cover
check_ops = type('Mock', (object,), {'assert_proper_iterable': lambda x: x if hasattr(x, '__iter__') else (_ for _ in ()).throw(TypeError('to be iterable'))})() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
