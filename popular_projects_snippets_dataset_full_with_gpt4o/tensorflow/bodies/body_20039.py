# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Create `TPUEmbeddingConfiguration`."""
config_proto = elc.TPUEmbeddingConfiguration()
for table in self._table_to_config_dict:
    table_descriptor = config_proto.table_descriptor.add()
    table_descriptor.name = table

    table_config = self._table_to_config_dict[table]
    # For small tables, we pad to the number of hosts so that at least one
    # id will be assigned to each host.
    table_descriptor.vocabulary_size = max(table_config.vocabulary_size,
                                           len(self.hosts))
    table_descriptor.dimension = table_config.dimension

    optimization_parameters = (
        self._optimizer_handler_dict[table].get_optimization_parameters())

    parameters = table_descriptor.optimization_parameters
    if table_config.learning_rate:
        parameters.learning_rate.constant = table_config.learning_rate
    elif table_config.learning_rate_fn:
        parameters.learning_rate.dynamic.tag = (
            self._learning_rate_fn_to_tag[table_config.learning_rate_fn])
    else:
        parameters.learning_rate.constant = (
            optimization_parameters.learning_rate)
    parameters.gradient_accumulation_status = (
        optimization_parameters_pb2.GradientAccumulationStatus.ENABLED
        if optimization_parameters.use_gradient_accumulation else
        optimization_parameters_pb2.GradientAccumulationStatus.DISABLED)

    if optimization_parameters.clip_gradient_min is not None:
        parameters.gradient_clipping_limits.lower.value = (
            optimization_parameters.clip_gradient_min)
    if optimization_parameters.clip_gradient_max is not None:
        parameters.gradient_clipping_limits.upper.value = (
            optimization_parameters.clip_gradient_max)

    if optimization_parameters.clip_weight_min is not None:
        parameters.clipping_limits.lower.value = (
            optimization_parameters.clip_weight_min)
    if optimization_parameters.clip_weight_max is not None:
        parameters.clipping_limits.upper.value = (
            optimization_parameters.clip_weight_max)
    if optimization_parameters.weight_decay_factor:
        parameters.weight_decay_factor = (
            optimization_parameters.weight_decay_factor)
        if (optimization_parameters
            .multiply_weight_decay_factor_by_learning_rate):
            parameters.multiply_weight_decay_factor_by_learning_rate = True
    if table_config.hot_id_replication:
        parameters.hot_id_replication_configuration.status = (
            optimization_parameters_pb2.HotIdReplicationConfiguration.ENABLED)
    optimizer_handler = self._optimizer_handler_dict[table]
    optimizer_handler.set_optimization_parameters(table_descriptor)

table_to_id = {
    table: i for i, table in enumerate(self._table_to_config_dict)
}

# Set feature descriptor field in the config proto.
for table in self._table_to_features_dict:
    features = self._table_to_features_dict[table]
    for feature in features:
        feature_descriptor = config_proto.feature_descriptor.add()

        feature_descriptor.table_id = table_to_id[
            self._feature_to_config_dict[feature].table_id]
        if self._feature_to_config_dict[feature].max_sequence_length > 0:
            feature_descriptor.input_shape.extend([
                self._batch_size_per_core,
                self._feature_to_config_dict[feature].max_sequence_length
            ])
        else:
            feature_descriptor.input_shape.extend([self._batch_size_per_core])

config_proto.mode = self._mode
config_proto.num_hosts = self._num_hosts
config_proto.num_tensor_cores = self._num_cores
config_proto.sharding_strategy = (
    elc.TPUEmbeddingConfiguration.DIV_DEFAULT if self._partition_strategy
    == 'div' else elc.TPUEmbeddingConfiguration.MOD)
config_proto.pipeline_execution_with_tensor_core = (
    self._pipeline_execution_with_tensor_core)
if self._profile_data_directory:
    config_proto.profile_data_directory = self._profile_data_directory

exit(config_proto)
