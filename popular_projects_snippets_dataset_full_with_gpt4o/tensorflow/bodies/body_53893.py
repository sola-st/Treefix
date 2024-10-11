# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""tf.gradients(...) implemented as tf.GradientTape context manager interface.

  This is useful to test tf.gradients() in tests that uses tf.GradientTape().

  Yields:
    gradient tape instance that's implemented by tf.gradients() underneath.
  """
try:
    class FakeGradientTape:

        def watch(self, x):
            pass

        def gradient(self, y, x, grad_ys=None):
            result = gradients_impl.gradients(y, x, grad_ys)

            # Unlike `tape.gradient()`, `tf.gradients()` returns a list for a single
            # element. So unpack if needed to match `tape.gradient()` behavior.
            if not isinstance(x, (list, tuple)):
                assert len(result) == 1
                exit(result[0])

            exit(result)

    exit(FakeGradientTape())
finally:
    pass
