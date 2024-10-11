# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes init_op.

    Args:
      init_op: `Operation` to initialize the variables. If set to USE_DEFAULT,
        create an op that initializes all variables and tables.
      init_feed_dict: A dictionary that maps `Tensor` objects to feed values.
        This feed dictionary will be used when `init_op` is evaluated.
    """
if init_op is Supervisor.USE_DEFAULT:
    init_op = self._get_first_op_from_collection(ops.GraphKeys.INIT_OP)
    if init_op is None:
        init_op = variables.global_variables_initializer()
        ops.add_to_collection(ops.GraphKeys.INIT_OP, init_op)
self._init_op = init_op
self._init_feed_dict = init_feed_dict
