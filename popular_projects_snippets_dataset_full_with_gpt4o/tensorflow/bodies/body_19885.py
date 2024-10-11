# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Create variables for TPU embeddings.

    Note under TPUStrategy this will ensure that all creations happen within a
    variable creation scope of the sharded variable creator.

    Returns:
      A dict of dicts. The outer dict is keyed by the table names and the inner
      dicts are keyed by 'parameters' and the slot variable names.
    """

def create_variables(table):
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

# Store tables based on name rather than TableConfig as we can't track
# through dicts with non-string keys, i.e. we won't be able to save.
variables = {}
for table in self._table_config:
    if not self._using_tpu:
        variables[table.name] = create_variables(table)
    else:
        with variable_scope.variable_creator_scope(
            make_sharded_variable_creator(self._hosts)):
            variables[table.name] = create_variables(table)

exit(variables)
