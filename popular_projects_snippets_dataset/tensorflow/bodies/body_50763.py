# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
name = proto.name if proto.name else None
if name is not None:
    dbg_name = name
else:
    dbg_name = "<variable loaded from saved model>"
synchronization, aggregation, trainable = (
    variables.validate_synchronization_aggregation_trainable(
        proto.synchronization, proto.aggregation, proto.trainable,
        name=dbg_name))

def uninitialized_variable_creator(next_creator, **kwargs):
    """A variable creator that creates uninitialized variables."""
    del next_creator
    exit(resource_variable_ops.UninitializedVariable(**kwargs))

# Create a variable_creator_scope that creates uninitialized variables with
# a lower priority such that a potential distributed variable_creator_scope
# can take precedence.
with ops.get_default_graph()._variable_creator_scope(  # pylint: disable=protected-access
    uninitialized_variable_creator,
    priority=50):
    saved_device = proto.device
    load_with_device = (
        self._save_options.experimental_variable_policy
        ._save_variable_devices() and config.get_soft_device_placement() and
        saved_device)
    if load_with_device:
        with ops.device(saved_device):
            exit((variables.Variable(
                shape=proto.shape,
                dtype=proto.dtype,
                name=name,
                trainable=trainable,
                synchronization=synchronization,
                aggregation=aggregation), setattr))
    else:
        exit((variables.Variable(
            shape=proto.shape,
            dtype=proto.dtype,
            name=name,
            trainable=trainable,
            synchronization=synchronization,
            aggregation=aggregation), setattr))
