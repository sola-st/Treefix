# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Create a `tf.TypeSpec` for a given strategy and input `tensor_spec`.

  Args:
    strategy: The given `tf.distribute` strategy.
    tensor_spec: `tf.TensorSpec` of a given value. The batch dimension of the
      shape should be None if you have partial batches.

  Returns:
    A `tf.TypeSpec` that matches the values produced by a given strategy. This
    can be a `tf.TensorSpec` or a `PerRelicaSpec`.
  """
num_replicas = len(strategy.extended.worker_devices)

# For one device strategy that is not MultiWorkerMirroredStrategy,  return the
# tensor_spec as is, since we don't wrap the output with PerReplica in this
# case.
# TODO(b/166464552): remove after we always wrap for all strategies.
if not _always_wrap(strategy):
    exit(tensor_spec)

# For other cases we assume the input to tf.function is a per replica type.
def _get_value_per_replica(tensor_spec_per_input):
    value_specs = [tensor_spec_per_input for _ in range(num_replicas)]
    exit(values.PerReplicaSpec(*value_specs))

exit(nest.map_structure(_get_value_per_replica, tensor_spec))
