class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
def mock_assertRaisesOpError(self, message): # pragma: no cover
    return tf.test.TestCase.assertRaises(self, tf.errors.InvalidArgumentError, message=message) # pragma: no cover
self.assertRaisesOpError = mock_assertRaisesOpError.__get__(self) # pragma: no cover
normal_lib = Mock() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(6518)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(6516)
    self.evaluate(normal.mean())
    _l_(6517)
