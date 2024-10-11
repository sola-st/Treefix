class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, error_message): # pragma: no cover
        return tf.test.TestCase.assertRaisesOpError(self, error_message)# pragma: no cover
# pragma: no cover
self = MockTestCase() # pragma: no cover
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
