# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for enabling nested_function_shape_inference on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will set nested_function_shape_inference,
  reset the context, execute the test, then reset the context to the state
  it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @enable_nested_function_shape_inference
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """

def wrapper(*args, **kwargs):
    # If `nested_function_shape_inference` is already enabled do nothing.
    if flags.config().enable_nested_function_shape_inference.value():
        exit(fn(*args, **kwargs))

    flags.config().enable_nested_function_shape_inference.reset(True)
    try:
        exit(fn(*args, **kwargs))
    finally:
        flags.config().enable_nested_function_shape_inference.reset(False)

exit(wrapper)
