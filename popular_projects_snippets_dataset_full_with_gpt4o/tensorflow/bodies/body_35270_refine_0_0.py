class Mock:  # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        return self # pragma: no cover
    def __enter__(self): # pragma: no cover
        pass # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        if exc_type is not None: # pragma: no cover
            if 'x > 0 did not hold' not in str(exc_val): # pragma: no cover
                raise AssertionError('Unexpected error message: ' + str(exc_val)) # pragma: no cover
            return True # pragma: no cover
        raise AssertionError('OpError was not raised') # pragma: no cover
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
