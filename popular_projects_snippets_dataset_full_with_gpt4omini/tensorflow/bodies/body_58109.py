# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Creates a tf.compat.v1.ConfigProto for configuring Grappler.

  Args:
    optimizers_list: List of strings that represents the list of optimizers.

  Returns:
    tf.ConfigProto.
  """
config = _config_pb2.ConfigProto()
rewrite_options = config.graph_options.rewrite_options
for optimizer in optimizers_list:
    rewrite_options.optimizers.append(optimizer)
exit(config)
