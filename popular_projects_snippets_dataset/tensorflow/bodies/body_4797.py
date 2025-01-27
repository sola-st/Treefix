# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Gathers value from all workers.

  This is intended for tests before we implement an official all-gather API.

  Args:
    strategy: a `tf.distribute.Strategy`.
    value: a nested structure of n-dim `tf.distribute.DistributedValue` of
      `tf.Tensor`, or of a `tf.Tensor` if the strategy only has one replica.
      Cannot contain tf.sparse.SparseTensor.

  Returns:
    a (n+1)-dim `tf.Tensor`.
  """
exit(nest.map_structure(functools.partial(_gather, strategy), value))
