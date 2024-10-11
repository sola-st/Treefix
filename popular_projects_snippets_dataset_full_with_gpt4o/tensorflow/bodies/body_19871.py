# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Creates the TPUEmbedding mid level API object.

    ```python
    strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(
          feature_config=tf.tpu.experimental.embedding.FeatureConfig(
              table=tf.tpu.experimental.embedding.TableConfig(
                  dim=...,
                  vocabulary_size=...)))
    ```

    Args:
      feature_config: A nested structure of
        `tf.tpu.experimental.embedding.FeatureConfig` configs.
      optimizer: An instance of one of `tf.tpu.experimental.embedding.SGD`,
        `tf.tpu.experimental.embedding.Adagrad` or
        `tf.tpu.experimental.embedding.Adam`. When not created under
        TPUStrategy may be set to None to avoid the creation of the optimizer
        slot variables, useful for optimizing memory consumption when exporting
        the model for serving where slot variables aren't needed.
      pipeline_execution_with_tensor_core: If True, the TPU embedding
        computations will overlap with the TensorCore computations (and hence
        will be one step old). Set to True for improved performance.

    Raises:
      ValueError: If optimizer is not one of tf.tpu.experimental.embedding.(SGD,
      Adam or Adagrad) or None when created under a TPUStrategy.
    """
self._strategy = distribution_strategy_context.get_strategy()
self._using_tpu = isinstance(self._strategy, (tpu_strategy.TPUStrategy,
                                              tpu_strategy.TPUStrategyV2))
self._pipeline_execution_with_tensor_core = (
    pipeline_execution_with_tensor_core)

self._feature_config = feature_config
self._output_shapes = []
for feature in nest.flatten(feature_config):
    self._output_shapes.append(feature.output_shape)

# The TPU embedding ops are slightly inconsistent with how they refer to
# tables:
# * The enqueue op takes a parallel list of tensors for input, one of those
#   is the table id for the feature which matches the integer index of the
#   table in the proto created by _create_config_proto().
# * The recv_tpu_embedding_activations op emits lookups per table in the
#   order from the config proto.
# * The send_tpu_embedding_gradients expects input tensors to be per table
#   in the same order as the config proto.
# * Per optimizer load and retrieve ops are specified per table and take the
#   table name rather than the table id.
# Thus we must fix a common order to tables and ensure they have unique
# names.

# Set table order here to the order of the first occurence of the table in a
# feature provided by the user. The order of this struct must be fixed
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
    if ((table.optimizer is not None or self._using_tpu) and
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

if self._using_tpu:
    # Extract a list of callable learning rates also in fixed order. Each
    # table in the config proto will get a index into this list and we will
    # pass this list in the same order after evaluation to the
    # send_tpu_embedding_gradients op.
    self._dynamic_learning_rates = []
    for table in self._table_config:
        if (callable(table.optimizer.learning_rate) and
            table.optimizer.learning_rate not in self._dynamic_learning_rates):
            self._dynamic_learning_rates.append(table.optimizer.learning_rate)

      # We need to list of host devices for the load/retrieve operations.
    self._hosts = get_list_of_hosts(self._strategy)

self._built = False
self._verify_output_shapes_on_enqueue = True
