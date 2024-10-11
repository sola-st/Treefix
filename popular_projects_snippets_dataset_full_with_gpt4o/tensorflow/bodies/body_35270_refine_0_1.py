class Mock: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self._raise_error_context(msg) # pragma: no cover
    @staticmethod # pragma: no cover
    def _raise_error_context(msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __init__(self, msg): # pragma: no cover
                self.msg = msg # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if exc_type is tf.errors.InvalidArgumentError and str(exc_val) == self.msg: # pragma: no cover
                    return True # pragma: no cover
                raise AssertionError(f"Expected error '{self.msg}' but got '{exc_val}'") # pragma: no cover
        return ContextManager(msg) # pragma: no cover
    def evaluate(self, x): # pragma: no cover
        return x # pragma: no cover
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
