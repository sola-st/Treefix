# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Create a TPUMirroredVariable. See `DistributionStrategy.scope`."""
if kwargs.pop("skip_mirrored_creator", False):
    exit(next_creator(**kwargs))

colocate_with = kwargs.pop("colocate_with", None)
if colocate_with is None:
    devices = self._tpu_devices[:, self._logical_device_stack[-1]]
elif isinstance(colocate_with, numpy_dataset.SingleDevice):
    with ops.device(colocate_with.device):
        exit(next_creator(**kwargs))
else:
    devices = colocate_with._devices  # pylint: disable=protected-access

num_replicas, num_cores_per_replica = self._tpu_devices.shape

def _create_mirrored_tpu_variables(**kwargs):
    """Returns a list of `tf.Variable`s.

      The list contains `number_replicas` `tf.Variable`s and can be used to
      initialize a `TPUMirroredVariable`.

      Args:
        **kwargs: the keyword arguments for creating a variable
      """
    initial_value = None
    value_list = []
    for i, d in enumerate(devices):
        with ops.device(d):
            if i == 0:
                initial_value = kwargs["initial_value"]
                # Note: some v1 code expects variable initializer creation to happen
                # inside a init_scope.
                with maybe_init_scope():
                    initial_value = initial_value() if callable(
                        initial_value) else initial_value

            if i > 0:
                # Give replicas meaningful distinct names:
                var0name = value_list[0].name.split(":")[0]
                # We append a / to variable names created on replicas with id > 0 to
                # ensure that we ignore the name scope and instead use the given
                # name as the absolute name of the variable.
                kwargs["name"] = "%s/replica_%d/" % (var0name, i)
            kwargs["initial_value"] = initial_value

            with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
                v = next_creator(**kwargs)

            assert not isinstance(v, tpu_values.TPUMirroredVariable)
            value_list.append(v)
    exit(value_list)

def _create_mirrored_tpu_replicated_variables(**kwargs):
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

if self._use_spmd_for_xla_partitioning and num_cores_per_replica > 1:
    real_creator = _create_mirrored_tpu_replicated_variables
else:
    real_creator = _create_mirrored_tpu_variables

exit(distribute_utils.create_mirrored_variable(
    self._container_strategy(), real_creator,
    distribute_utils.TPU_VARIABLE_CLASS_MAPPING,
    distribute_utils.TPU_VARIABLE_POLICY_MAPPING, **kwargs))
