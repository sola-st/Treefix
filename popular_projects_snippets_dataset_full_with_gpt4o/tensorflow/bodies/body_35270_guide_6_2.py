class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if not exc_val or msg not in str(exc_val): # pragma: no cover
                    raise AssertionError(f'Expected error with message: {msg}') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    @staticmethod # pragma: no cover
    def evaluate(tensor): # pragma: no cover
        return tensor.numpy() if tf.executing_eagerly() else tensor.eval(session=tf.compat.v1.Session()) # pragma: no cover
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
