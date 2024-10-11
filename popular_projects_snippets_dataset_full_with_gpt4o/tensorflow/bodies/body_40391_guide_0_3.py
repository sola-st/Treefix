class MockSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def assertRaisesRegex(*args, **kwargs): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self2): # pragma: no cover
                return None # pragma: no cover
            def __exit__(self2, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, ValueError): # pragma: no cover
                    raise AssertionError(f'ValueError not raised, but {exc_type} was raised instead.') # pragma: no cover
                if not kwargs['expected_regex'] in str(exc_value): # pragma: no cover
                    pass
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
from l3.Runtime import _l_
x = constant_op.constant(1.0)
_l_(22428)
y = constant_op.constant(1.0)
_l_(22429)
with backprop.GradientTape() as g:
    _l_(22432)

    g.watch([x, y])
    _l_(22430)
    z = y * 2
    _l_(22431)
with self.assertRaisesRegex(
    ValueError, "Unknown value for unconnected_gradients: 'nonsense'"):
    _l_(22434)

    g.gradient(z, x, unconnected_gradients='nonsense')
    _l_(22433)
