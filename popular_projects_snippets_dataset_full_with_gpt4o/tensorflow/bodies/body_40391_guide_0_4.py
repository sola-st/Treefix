class MockTestCase: # pragma: no cover
    def assertRaisesRegex(self, exception, regex): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception) or not regex in str(exc_val): # pragma: no cover
                    raise AssertionError('Expected exception but got different/wrong one') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover

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
