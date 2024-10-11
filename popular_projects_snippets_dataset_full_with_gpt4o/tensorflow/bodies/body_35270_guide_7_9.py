class MockTestCase: # pragma: no cover
    def assertRaisesOpError(self, msg): # pragma: no cover
        @contextlib.contextmanager # pragma: no cover
        def context_manager(): # pragma: no cover
            try: # pragma: no cover
                yield # pragma: no cover
            except tf.errors.InvalidArgumentError as e: # pragma: no cover
                if msg in str(e): # pragma: no cover
                    return # pragma: no cover
                raise AssertionError(f"Expected message '{msg}' not found in '{str(e)}'") from e # pragma: no cover
            raise AssertionError(f"Expected tf.errors.InvalidArgumentError not raised") # pragma: no cover
        return context_manager() # pragma: no cover
    @staticmethod # pragma: no cover
    def evaluate(tensor): # pragma: no cover
        return tensor.numpy() if tf.executing_eagerly() else tf.get_static_value(tensor) # pragma: no cover
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
