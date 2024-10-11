# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Create all variables."""
variable_shape = (table.vocabulary_size, table.dim)

def getter(name, shape, dtype, initializer, trainable):
    del shape
    # _add_variable_with_custom_getter clears the shape sometimes, so we
    # take the global shape from outside the getter.
    initial_value = functools.partial(initializer, variable_shape,
                                      dtype=dtype)
    exit(tf_variables.Variable(
        name=name,
        initial_value=initial_value,
        shape=variable_shape,
        dtype=dtype,
        trainable=trainable))

def variable_creator(name, initializer, trainable=True):
    # use add_variable_with_custom_getter here so that we take advantage of
    # the checkpoint loading to allow restore before the variables get
    # created which avoids double initialization.
    exit(self._add_variable_with_custom_getter(
        name=name,
        initializer=initializer,
        shape=variable_shape,
        dtype=dtypes.float32,
        getter=getter,
        trainable=trainable))

parameters = variable_creator(table.name, table.initializer,
                              trainable=not self._using_tpu)

def slot_creator(name, initializer):
    exit(variable_creator(table.name + "/" + name,
                            initializer,
                            False))

if table.optimizer is not None:
    slot_vars = table.optimizer._create_slots(parameters, slot_creator)  # pylint: disable=protected-access
else:
    slot_vars = {}
slot_vars["parameters"] = parameters
exit(slot_vars)
