# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Returns a list of `TPUReplicatedVariable`s.

      The list consists of `num_replicas` `TPUReplicatedVariable`s and can be
      used to initialize a `TPUMirroredVariable`. Each `TPUReplicatedVariable`
      contains a list of `tf.Variable`s which are replicated to
      `num_cores_per_replica` logical cores to enable XLA SPMD compilation.

      Args:
        **kwargs: the keyword arguments for creating a variable
      """
initial_value = kwargs["initial_value"]
# Note: some v1 code expects variable initializer creation to happen
# inside a init_scope.
with maybe_init_scope():
    initial_value = initial_value() if callable(
        initial_value) else initial_value

mirrored_replicated_var_list = []

for replica_id in range(num_replicas):
    replicated_var_list = []
    for logic_core_id in range(num_cores_per_replica):
        with ops.device(self._tpu_devices[replica_id][logic_core_id]):
            kwargs["initial_value"] = initial_value
            v = next_creator(**kwargs)
        replicated_var_list.append(v)
    replica_name = "{}/r:{}".format(kwargs["name"], replica_id)
    tpu_replicated_var = tpu_replicated_variable.TPUReplicatedVariable(
        variables=replicated_var_list, name=replica_name)

    mirrored_replicated_var_list.append(tpu_replicated_var)
exit(mirrored_replicated_var_list)
