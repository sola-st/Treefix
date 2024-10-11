# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for enabling quantized_dtypes_training on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will set quantized_dtypes_training,
  reset the context, execute the test, then reset the context to the state
  it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @enable_quantized_dtypes_training
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """

def wrapper(*args, **kwargs):
    # If `enable_quantized_dtypes_training` is already enabled do nothing.
    if flags.config().enable_quantized_dtypes_training.value():
        exit(fn(*args, **kwargs))

    flags.config().enable_quantized_dtypes_training.reset(True)
    try:
        exit(fn(*args, **kwargs))
    finally:
        flags.config().enable_quantized_dtypes_training.reset(False)

exit(wrapper)
