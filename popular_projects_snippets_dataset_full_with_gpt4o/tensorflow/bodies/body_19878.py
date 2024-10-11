# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Creates the TPUEmbeddingConfiguration proto.

    This proto is used to initialize the TPU embedding engine.

    Returns:
      A TPUEmbeddingConfiguration proto.
    """

config_proto = tpu_embedding_configuration_pb2.TPUEmbeddingConfiguration()

# Map each callable dynamic learning rate to its in index in the list.
# The learning rate index is the index of the dynamic learning rate for this
# table (if it exists) in the list we created at initialization. We don't
# simply create one learning rate index per table as this has extremely bad
# performance characteristics. The more separate optimization configurations
# we have, the worse the performance will be.
learning_rate_index = {r: i for i, r in enumerate(
    self._dynamic_learning_rates)}

for table in self._table_config:
    table._set_table_descriptor(  # pylint: disable=protected-access
        config_proto.table_descriptor.add(),
        self._strategy.extended.num_hosts,
        learning_rate_index)

table_to_id = {table: i for i, table in enumerate(self._table_config)}

# Set feature descriptor field in the config proto.
for feature, output_shape in zip(
    nest.flatten(self._feature_config), self._output_shapes):
    feature_descriptor = config_proto.feature_descriptor.add()

    if feature.name:
        feature_descriptor.name = feature.name

    feature_descriptor.table_id = table_to_id[feature.table]
    # The input shape of the feature is the actual shape of the input tensor
    # except the last dimension because the last dimension will always be
    # reduced.
    feature_descriptor.input_shape.extend(output_shape.as_list())

# Always set mode to training, we override the mode during enqueue.
config_proto.mode = (
    tpu_embedding_configuration_pb2.TPUEmbeddingConfiguration.TRAINING)

config_proto.num_hosts = self._strategy.extended.num_hosts
config_proto.num_tensor_cores = self._strategy.num_replicas_in_sync

# TODO(bfontain): Allow users to pick MOD for the host sharding.
config_proto.sharding_strategy = (
    tpu_embedding_configuration_pb2.TPUEmbeddingConfiguration.DIV_DEFAULT)
config_proto.pipeline_execution_with_tensor_core = (
    self._pipeline_execution_with_tensor_core)

exit(config_proto)
