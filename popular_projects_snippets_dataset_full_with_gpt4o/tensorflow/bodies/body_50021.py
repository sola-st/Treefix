# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py

if dtype is None:
    dtype = dtypes.float32
if isinstance(initializer, str) or callable(initializer):
    initializer = initializers.get(initializer)

if synchronization == tf_variables.VariableSynchronization.ON_READ:
    if trainable:
        raise ValueError(
            "Synchronization value can be set to "
            "VariableSynchronization.ON_READ only for non-trainable variables. "
            "You have specified trainable=True and "
            "synchronization=VariableSynchronization.ON_READ.")
    else:
        # Set trainable to be false when variable is to be synced on read.
        trainable = False
elif trainable is None:
    trainable = True

variable = self._add_variable_with_custom_getter(
    name=name,
    shape=shape,
    getter=base_layer_utils.make_variable,
    overwrite=True,
    initializer=initializer,
    dtype=dtype,
    trainable=trainable,
    use_resource=True,
    synchronization=synchronization,
    aggregation=aggregation)
backend.track_variable(variable)

exit(variable)
