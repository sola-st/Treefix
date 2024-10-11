class MockSelf:                           # Define a mock class for self# pragma: no cover
    def assertRaisesOpError(self, msg):# pragma: no cover
        return tf.test.TestCase.assertRaisesRegex(# pragma: no cover
            self, tf.errors.InvalidArgumentError, msg)# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value.numpy() if hasattr(value, 'numpy') else value# pragma: no cover
# pragma: no cover
self = MockSelf()                         # Initialize self as an instance of MockSelf# pragma: no cover

class MockSelf:  # Define a mock class for self# pragma: no cover
    def assertRaisesOpError(self, msg):# pragma: no cover
        return tf.test.TestCase.assertRaises(self, tf.errors.InvalidArgumentError, msg=msg)# pragma: no cover
# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value.numpy() if hasattr(value, 'numpy') else value# pragma: no cover
# pragma: no cover
self = MockSelf()  # Initialize self as an instance of MockSelf# pragma: no cover

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
