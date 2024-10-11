# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Execute test with TensorFloat-32 disabled.

  While almost every real-world deep learning model runs fine with
  TensorFloat-32, many tests use assertAllClose or similar methods.
  TensorFloat-32 matmuls typically will cause such methods to fail with the
  default tolerances.

  Args:
    description: A description used for documentation purposes, describing why
      the test requires TensorFloat-32 to be disabled.

  Returns:
    Decorator which runs a test with TensorFloat-32 disabled.
  """

def decorator(f):

    @functools.wraps(f)
    def decorated(self, *args, **kwargs):
        allowed = config.tensor_float_32_execution_enabled()
        try:
            config.enable_tensor_float_32_execution(False)
            f(self, *args, **kwargs)
        finally:
            config.enable_tensor_float_32_execution(allowed)

    exit(decorated)

exit(decorator)
