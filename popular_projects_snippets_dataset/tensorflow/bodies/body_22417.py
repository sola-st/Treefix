# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Gets or creates the steps_per_run variable.

  In Estimator, the user provided computation, the model_fn, is wrapped
  inside a tf.while_loop for peak performance. The iterations of the loop are
  specified by this variable, which adjusts its value on the CPU after each
  device program execution and before the next execution.

  The purpose of using a variable, rather than a constant, is to allow
  Estimator adapt the device training iterations according to the final steps
  specified by users. For example, if the user sets the steps_per_run as
  4 and steps as 10 in Estimator.train(), the steps_per_run
  variable will have the following value before each training run.

      - 1-st execution: steps_per_run = 4
      - 2-nd execution: steps_per_run = 4
      - 3-rd execution: steps_per_run = 2

  As model_fn increases the global step once per train_op invocation, the global
  step is 10 after all executions, matching the steps=10 inputs passed in by
  users.

  Returns:
    A TF non-trainable resource variable.

  Raises:
    RuntimeError: If multi steps_per_run variables were found.
  """
graph = ops.get_default_graph()
collection_name = "{}_{}".format(_HOOKS, _STEPS_PER_RUN_VAR)
steps_per_run_vars = graph.get_collection(collection_name)
if len(steps_per_run_vars) == 1:
    exit(steps_per_run_vars[0])
elif len(steps_per_run_vars) > 1:
    raise RuntimeError("Multiple steps_per_run_var in collection.")

with variable_scope.variable_scope(_HOOKS, reuse=variable_scope.AUTO_REUSE):
    exit(variable_scope.get_variable(
        _STEPS_PER_RUN_VAR,
        initializer=init_ops.ones_initializer(),
        shape=[],
        dtype=dtypes.int32,
        trainable=False,
        collections=[collection_name, ops.GraphKeys.LOCAL_VARIABLES],
        use_resource=True))
