import unittest # pragma: no cover
import re # pragma: no cover

class MockCheckOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_proper_iterable(value): # pragma: no cover
        if not hasattr(value, '__iter__'): # pragma: no cover
            raise TypeError('Expected an object to be iterable') # pragma: no cover
 # pragma: no cover
check_ops = MockCheckOps() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, *args, **kwargs): # pragma: no cover
        if len(args) == 0: # pragma: no cover
            raise ValueError('assertRaisesRegex needs a callable as an argument') # pragma: no cover
        callable_obj = args[0] # pragma: no cover
        try: # pragma: no cover
            callable_obj() # pragma: no cover
        except expected_exception as e: # pragma: no cover
            if re.search(expected_regex, str(e)) is None: # pragma: no cover
                raise AssertionError(f'Exception message does not match: {e}') # pragma: no cover
        else: # pragma: no cover
            raise AssertionError('Expected exception was not raised') # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

import unittest # pragma: no cover
import re # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertRaisesRegex(self, expected_exception, expected_regex, callable_obj=None, *args, **kwargs): # pragma: no cover
        context = _AssertRaisesContext(expected_exception, self, callable_obj, expected_regex) # pragma: no cover
        return context.handle('assertRaisesRegex', callable_obj, args, kwargs) # pragma: no cover
 # pragma: no cover
class _AssertRaisesContext: # pragma: no cover
    def __init__(self, expected, test_case, callable_obj=None, expected_regex=None): # pragma: no cover
        self.expected = expected # pragma: no cover
        self.test_case = test_case # pragma: no cover
        self.expected_regex = expected_regex # pragma: no cover
        self.obj_name = getattr(callable_obj, '__name__', str(callable_obj)) # pragma: no cover
        self.callable_obj = callable_obj # pragma: no cover
        self.args = () # pragma: no cover
        self.kwargs = {} # pragma: no cover
 # pragma: no cover
    def __enter__(self): # pragma: no cover
        return self # pragma: no cover
 # pragma: no cover
    def __exit__(self, exc_type, exc_value, tb): # pragma: no cover
        if not exc_type: # pragma: no cover
            self.test_case.fail(f'{self.expected.__name__} not raised by {self.obj_name}') # pragma: no cover
        if not issubclass(exc_type, self.expected): # pragma: no cover
            return False # pragma: no cover
        if self.expected_regex and not re.search(self.expected_regex, str(exc_value)): # pragma: no cover
            self.test_case.fail(f'{exc_type.__name__} raised by {self.obj_name} does not match {self.expected_regex!r}') # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
def mock_assert_proper_iterable(x): # pragma: no cover
    if not hasattr(x, '__iter__'): # pragma: no cover
        raise TypeError('to be iterable') # pragma: no cover
 # pragma: no cover
check_ops = type('MockCheckOps', (object,), {'assert_proper_iterable': mock_assert_proper_iterable})() # pragma: no cover
self = MockTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
from l3.Runtime import _l_
non_iterable = 1234
_l_(22164)
with self.assertRaisesRegex(TypeError, "to be iterable"):
    _l_(22166)

    check_ops.assert_proper_iterable(non_iterable)
    _l_(22165)
