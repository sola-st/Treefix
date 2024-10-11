class MockBase(object): # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                pass # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is not tf.errors.CancelledError: # pragma: no cover
                    raise AssertionError(f"Exception type {exc_type} does not match tf.errors.CancelledError") # pragma: no cover
                if msg not in str(exc_value): # pragma: no cover
                    raise AssertionError(f"Message '{msg}' not found in exception '{exc_value}") # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        raise tf.errors.CancelledError(None, None, "Operation was cancelled") # pragma: no cover
 # pragma: no cover
self = type("Mock", (MockBase,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(17059)

    self.evaluate(takeg_op)
    _l_(17058)
