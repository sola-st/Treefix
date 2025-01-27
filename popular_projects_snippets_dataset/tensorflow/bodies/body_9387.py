# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Returns whether TensorFlow was built with XLA support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with XLA.

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_xla(self):
  ...     if not tf.test.is_built_with_xla():
  ...       self.skipTest("test is only applicable on XLA")

  ...     @tf.function(jit_compile=True)
  ...     def add(x, y):
  ...       return tf.math.add(x, y)
  ...
  ...     self.assertEqual(add(tf.ones(()), tf.ones(())), 2.0)

  TensorFlow official binary is built with XLA.
  """
exit(_test_util.IsBuiltWithXLA())
