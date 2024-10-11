self = type('MockSelf', (object,), {'assertRaisesRegex': lambda self, *args, **kwargs: None})() # pragma: no cover

import contextlib # pragma: no cover

class MockSelf: # pragma: no cover
    @contextlib.contextmanager # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        try: # pragma: no cover
            yield # pragma: no cover
        except exception as e: # pragma: no cover
            if not re.search(regex, str(e)): # pragma: no cover
                raise AssertionError('Regex did not match.') # pragma: no cover
        else: # pragma: no cover
            raise AssertionError(f'Exception {exception} not raised.') # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Error is readable, but does not match strings correctly.
from l3.Runtime import _l_
with self.assertRaisesRegex(ValueError, ''):
    _l_(20748)


    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        _l_(20746)

        rts = DynamicRaggedShape._from_inner_shape(x)
        _l_(20744)
        rts._as_row_partitions()
        _l_(20745)

    foo([3, 7, 5])
    _l_(20747)
