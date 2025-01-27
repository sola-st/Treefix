# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_base.py
"""Creates the TPUEmbeddingBase object."""
self._feature_config = feature_config
self._output_shapes = []
for feature in nest.flatten(feature_config):
    self._output_shapes.append(feature.output_shape)
# Set table order here to the order of the first occurrence of the table in
# a feature provided by the user. The order of this struct must be fixed
# to provide the user with deterministic behavior over multiple
# instantiations.
self._table_config = []
for feature in nest.flatten(feature_config):
    if feature.table not in self._table_config:
        self._table_config.append(feature.table)

    # Ensure tables have unique names. Also error check the optimizer as we
    # specifically don't do that in the TableConfig class to allow high level
    # APIs that are built on this to use strings/other classes to represent
    # optimizers (before they are passed to this class).
table_names = []
for i, table in enumerate(self._table_config):
    if table.optimizer is None:
        # TODO(bfontain) Should we allow some sort of optimizer merging here?
        table.optimizer = optimizer
    if (table.optimizer is not None and
        not isinstance(table.optimizer, tpu_embedding_v2_utils._Optimizer)):  # pylint: disable=protected-access
        raise ValueError("{} is an unsupported optimizer class. Please pass an "
                         "instance of one of the optimizer classes under "
                         "tf.tpu.experimental.embedding.".format(
                             type(table.optimizer)))
    if table.name is None:
        table.name = "table_{}".format(i)
    if table.name in table_names:
        raise ValueError("Tables must have a unique name. "
                         f"Multiple tables with name {table.name} found.")
    table_names.append(table.name)

self._built = False
