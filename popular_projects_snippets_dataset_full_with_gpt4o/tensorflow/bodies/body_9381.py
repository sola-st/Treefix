# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
"""Returns whether TensorFlow was built with CUDA (GPU) support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with CUDA (GPU).

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_cuda():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device("GPU:0"):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  TensorFlow official binary is built with CUDA.
  """
exit(_test_util.IsGoogleCudaEnabled())
