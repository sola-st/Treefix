# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribution_strategy_context.py
"""A context that forces SyncOnReadVariable to aggregate upon reading.

  This context is useful if one wants to read the aggregated value out of a
  SyncOnReadVariable in replica context. By default the aggregation is turned
  off per the definition of SyncOnReadVariable.

  When reading a SyncOnReadVariable in cross-replica context, aggregation is
  always turned on so there is no need for such context.

  By reading a SyncOnReadVariable, we mean:
    1. Convert the variable to a tensor using `convert_to_tensor`.
    2. Calling `variable.value()` or `variable.read_value()`.

  Example usage:

  ```
  strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
  with strategy.scope():
    v = tf.Variable(1.0, synchronization=tf.VariableSynchronization.ON_READ,
      aggregation=tf.VariableAggregation.SUM)

  def replica_fn():
    return v + 10.0

  non_aggregated = strategy.run(replica_fn)
  print(non_aggregated) # PerReplica: {0: 11.0, 1: 11.0}

  def replica_fn():
    with variable_sync_on_read_context():
      return v + 10.0

  aggregated = strategy.run(replica_fn)
  print(aggregated) # PerReplica: {0: 12.0, 1: 12.0}
  ```

  Yields:
    Context manager for aggregating SyncOnReadVariable upon reading.
  """
try:
    _variable_sync_on_read_context.entered = True
    exit()
finally:
    _variable_sync_on_read_context.entered = False
