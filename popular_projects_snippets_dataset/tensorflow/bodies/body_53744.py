# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for setting XLA_FLAGS prior to running a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will allow users to set any xla flags
  exposed via the XLA_FLAGS environment variable, execute the test, then reset
  the XLA_FLAGS to the state it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @set_xla_env_flag(flag='--xla_gpu_enable_fast_min_max=false')
    def testFoo(self):
      ...

  Args:
    func: The function to be wrapped.
    flag: The xla flag to be set in the XLA_FLAGS env variable.

  Returns:
    The wrapped function.
  """

def decorator(f):

    @functools.wraps(f)
    def decorated(*args, **kwargs):
        original_xla_flags = os.environ.get("XLA_FLAGS")
        new_xla_flags = flag
        if original_xla_flags:
            new_xla_flags = new_xla_flags + " " + original_xla_flags
        os.environ["XLA_FLAGS"] = new_xla_flags
        try:
            exit(f(*args, **kwargs))
        finally:
            if original_xla_flags is None:
                del os.environ["XLA_FLAGS"]
            else:
                os.environ["XLA_FLAGS"] = original_xla_flags

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
