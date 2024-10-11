class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_val or msg not in str(exc_val): # pragma: no cover
                    raise AssertionError(f'Expected error with message: {msg}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensorflow.get_static_value(tensor) # pragma: no cover
self = MockTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(18549)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(18547)
    self.evaluate(normal.mean())
    _l_(18548)
