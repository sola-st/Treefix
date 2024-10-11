is_built_with_cuda = lambda: True # pragma: no cover
is_built_with_rocm = lambda: False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
from l3.Runtime import _l_
"""Returns whether TensorFlow was built with GPU (CUDA or ROCm) support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with GPU.

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_gpu_support():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device("GPU:0"):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  TensorFlow official binary is built with CUDA GPU support.
  """
aux = is_built_with_cuda() or is_built_with_rocm()
_l_(22376)
exit(aux)
