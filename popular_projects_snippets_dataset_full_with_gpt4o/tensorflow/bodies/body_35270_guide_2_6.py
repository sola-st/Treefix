class Mock: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_value or msg not in str(exc_value): # pragma: no cover
                    raise AssertionError('Expected error message not found') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tf.convert_to_tensor(tensor).numpy() # pragma: no cover
self = Mock() # pragma: no cover

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
