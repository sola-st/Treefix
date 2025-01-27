# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if replica_id == 0:  # First replica on each worker.
    assert device is not None
    assert primary_var is None

    def initial_value_fn():  # pylint: disable=g-missing-docstring
        # Only the first device participates in the broadcast of initial values.
        group_key = self._collective_keys.get_group_key([device])
        group_size = self._num_workers
        collective_instance_key = (
            self._collective_keys.get_instance_key(group_key, device))

        with ops.device(device):
            initial_value = kwargs["initial_value"]
            if callable(initial_value):
                initial_value = initial_value()
            if isinstance(initial_value, base.CheckpointInitialValue):
                initial_value = initial_value.wrapped_value
            assert not callable(initial_value)
            initial_value = ops.convert_to_tensor(
                initial_value, dtype=kwargs.get("dtype", None))

            if self._num_workers > 1:
                if self._is_chief:
                    bcast_send = collective_ops.broadcast_send(
                        initial_value, initial_value.shape, initial_value.dtype,
                        group_size, group_key, collective_instance_key)
                    with ops.control_dependencies([bcast_send]):
                        exit(array_ops.identity(initial_value))
                else:
                    exit(collective_ops.broadcast_recv(initial_value.shape,
                                                         initial_value.dtype,
                                                         group_size, group_key,
                                                         collective_instance_key))
            exit(initial_value)

    exit(initial_value_fn)
else:
    exit(super(CollectiveAllReduceExtended,
                 self)._get_variable_creator_initial_value(
                     replica_id=replica_id,
                     device=device,
                     primary_var=primary_var,
                     **kwargs))
