# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Runs the decorated test twice--once as is, once inside a tf.function.

  This allows you to run a test both in eager execution and inside a
  tf.function, exercising the two execution modes supported in tf 2.0. The test
  assertions are automatically done inside tf.py_funcs, and tf.function ensures
  that they run in the proper order and with the proper side effects.

  Currently variable creation is not supported in tests annotated with this
  decorator since it's tricky to ensure the variable doesn't get repeatedly
  created when retracing the tf.function.

  Args:
    f: the test method to be decorated

  Returns:
    The decorated test method, which will run both in eager and inside a
    tf.function.
  """

def decorated(*args, **kwds):

    def bound_f():
        f(*args, **kwds)

    with context.eager_mode():
        # Running in eager mode
        bound_f()
        # Running as TF function
        # TODO(b/121143941): Remove the autograph override.
        def_function.function(bound_f, autograph=False)()

exit(decorated)
