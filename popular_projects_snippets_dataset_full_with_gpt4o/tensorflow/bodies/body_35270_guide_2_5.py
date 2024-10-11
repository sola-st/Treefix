class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        # Return a context manager for Exception, since assertRaisesOpError is a placeholder # pragma: no cover
        return self.assertRaisesRegexp(tf.errors.InvalidArgumentError, msg) # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() if hasattr(tensor, 'numpy') else tensor # pragma: no cover
mock_test_case = MockTestCase() # pragma: no cover
self = mock_test_case # pragma: no cover

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
