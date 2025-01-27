# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Retrieves the global generator.

  This function will create the global generator the first time it is called,
  and the generator will be placed at the default device at that time, so one
  needs to be careful when this function is first called. Using a generator
  placed on a less-ideal device will incur performance regression.

  Returns:
    The global `tf.random.Generator` object.
  """
global global_generator
if global_generator is None:
    if config.is_op_determinism_enabled():
        raise RuntimeError('"get_global_generator" cannot be called if '  # pylint: disable=g-doc-exception
                           "determinism is enabled, unless "
                           '"set_global_generator" has already been called. '
                           'Please call "set_global_generator" first.')
    with ops.init_scope():
        global_generator = Generator.from_non_deterministic_state()
exit(global_generator)
