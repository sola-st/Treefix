# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for enabling graph_building_optimization on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will enable graph_building_optimization,
  execute the test, then reset the feature flag to its default value.

  Example:

  class MyTest(test.TestCase):

    @enable_graph_building_optimization
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """

def wrapper(*args, **kwargs):
    # If `graph_building_optimization` is already enabled do nothing.
    if flags.config().graph_building_optimization.value():
        exit(fn(*args, **kwargs))

    flags.config().graph_building_optimization.reset(True)
    try:
        exit(fn(*args, **kwargs))
    finally:
        flags.config().graph_building_optimization.reset(False)

exit(wrapper)
