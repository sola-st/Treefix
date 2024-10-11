# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Runs functions eagerly if `run_eagerly` is true.

  WARNING: Setting `run_eagerly` to True in tests running in V1 graph mode
  *WILL NOT* make the tf.function to run eagerly because eager is disabled by
  default in V1. Instead, tf.function will run as a traced graph function.

  Ensures that the state (for running functions eagerly) is back to the initial
  `def_function.RUN_FUNCTIONS_EAGERLY` state.

  Args:
    run_eagerly: Boolean determining whether to run the function eagerly or not.

  Raises:
    ValueError if `run_eagerly` is not a boolean.

  Yields:
    Nothing.
  """
if not isinstance(run_eagerly, bool):
    raise ValueError(
        "Expected bool for `run_eagerly` but got {}".format(run_eagerly))

is_eager = context.executing_eagerly()
if not is_eager and run_eagerly:
    logging.warning(
        "Running tf.function eagerly in V1 graph mode is not supported. "
        "tf.function will be run as a traced graph function.")

initial_state = def_function.functions_run_eagerly()
def_function.run_functions_eagerly(run_eagerly)
try:
    exit()
finally:
    def_function.run_functions_eagerly(initial_state)
