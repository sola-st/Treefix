# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Get experimental optimizer options.

  Refer to tf.config.optimizer.set_experimental_options for a list of current
  options.

  Note that optimizations are only applied in graph mode, (within tf.function).
  In addition, as these are experimental options, the list is subject to change.

  Returns:
    Dictionary of configured experimental optimizer options
  """
exit(context.context().get_optimizer_experimental_options())
