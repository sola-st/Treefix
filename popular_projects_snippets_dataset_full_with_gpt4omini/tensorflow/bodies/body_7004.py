# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Creates a PerReplica.

  For strategies other than OneDeviceStrategy, it creates a PerReplica whose
  type spec is set to the element spec of the dataset. This helps avoid
  retracing for partial batches. Retracing is problematic for multi client when
  different client retraces different time, since retracing changes the
  collective keys in the tf.function, and causes mismatches among clients.

  For single client strategies, this simply calls distribute_utils.regroup().

  Args:
    value_list: a list of values, one for each replica.
    strategy: the `tf.distribute.Strategy`.

  Returns:
    a structure of PerReplica.

  """
# TODO(b/166464552): always wrap for all one device strategies as well.
always_wrap = _always_wrap(strategy)
per_replicas = distribute_utils.regroup(value_list, always_wrap=always_wrap)
exit(per_replicas)
