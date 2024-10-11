# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""API for using TPU for embedding lookups.

    Args:
      table_to_config_dict: A dictionary mapping from string of table name to
        `TableConfig`. Table refers to an embedding table, e.g. `params`
        argument to `tf.nn.embedding_lookup_sparse()`.
      feature_to_config_dict: A dictionary mapping from string of feature name
        to `FeatureConfig`. Feature refers to ids to lookup in embedding table,
        e.g. `sp_ids` argument to `tf.nn.embedding_lookup_sparse()`.
      batch_size: An `int` representing the global batch size.
      mode: `TRAINING` or `INFERENCE`.
      master: A `string` representing the TensorFlow master to use.
      optimization_parameters: `AdagradParameters`, `AdamParameters`,
        `Stochasticgradientdescentparameters`. Must be set in training unless
        all tables specify their own optimizers. And it must be `None` in
        inference.
      cluster_def: A ClusterDef object describing the TPU cluster.
      pipeline_execution_with_tensor_core: setting this to `True` makes training
        faster, but trained model will be different if step N and step N+1
        involve the same set of embedding IDs. Please see
        `tpu_embedding_configuration.proto` for details.
      partition_strategy: A string, either 'mod' or 'div', specifying how to map
        the lookup id to the embedding tensor. For more information see
        `tf.nn.embedding_lookup_sparse`.
      profile_data_directory: Directory where embedding lookup statistics are
        stored. These statistics summarize information about the inputs to the
        embedding lookup operation, in particular, the average number of
        embedding IDs per example and how well the embedding IDs are load
        balanced across the system. The lookup statistics are used during TPU
        initialization for embedding table partitioning. Collection of lookup
        statistics is done at runtime by  profiling the embedding inputs, only a
        small fraction of input samples are profiled to minimize host CPU
        overhead. Once a suitable number of samples are profiled, the lookup
        statistics are saved to table-specific files in the profile data
        directory generally at the end of a TPU training loop. The filename
        corresponding to each table is obtained by hashing table specific
        parameters (e.g., table name and number of features) and global
        configuration parameters (e.g., sharding strategy and task count). The
        same profile data directory can be shared among several models to reuse
        embedding lookup statistics.
      device_config: A DeviceConfig instance, used when `master` and
        `cluster_def` are both `None`.
      master_job_name: if set, overrides the master job name used to schedule
        embedding ops.

    Raises:
      ValueError: if any input is invalid.
    """
if partition_strategy not in ('div', 'mod'):
    raise ValueError(f'partition_strategy must be "div" or "mod". '
                     f'Received: {partition_strategy}.')
self._partition_strategy = partition_strategy

self._profile_data_directory = profile_data_directory

_validate_table_to_config_dict(table_to_config_dict)
# Avoid nondeterminism from `Dict` iteration order by using `OrderedDict`.
self._table_to_config_dict = _create_ordered_dict(table_to_config_dict)

_validate_feature_to_config_dict(table_to_config_dict,
                                 feature_to_config_dict)
self._feature_to_config_dict = _create_ordered_dict(feature_to_config_dict)
self._table_to_features_dict = (
    _create_table_to_features_dict(self._feature_to_config_dict))
self._combiners = _create_combiners(self._table_to_config_dict,
                                    self._table_to_features_dict)

self._batch_size = batch_size

if master is None and cluster_def is None:
    if device_config is None:
        raise ValueError('When master and cluster_def are both None,'
                         'device_config must be set but is not.')
    if device_config.num_cores % device_config.num_hosts:
        raise ValueError('num_hosts ({}) should divide num_cores ({}) '
                         'but does not.'.format(device_config.num_cores,
                                                device_config.num_hosts))
    self._num_hosts = device_config.num_hosts
    self._num_cores = device_config.num_cores
    self._num_cores_per_host = self._num_cores // self._num_hosts
    self._hosts = [
        '{}/replica:0/task:{}/device:CPU:0'.format(device_config.job_name, i)
        for i in range(self._num_hosts)
    ]
else:
    tpu_system_metadata = (
        tpu_system_metadata_lib._query_tpu_system_metadata(  # pylint: disable=protected-access
            master,
            cluster_def=cluster_def))
    if tpu_system_metadata.num_cores == 0:
        raise ValueError('TPUEmbedding needs TPUs, but master {} does not have '
                         'TPUs.'.format(master))
    self._num_hosts = tpu_system_metadata.num_hosts
    if master_job_name is None:
        try:
            master_job_name = tpu_system_metadata_lib.master_job(
                master, cluster_def)
        except ValueError as e:
            raise ValueError(str(e) + ' Please specify a master_job_name.')
    self._hosts = []
    for device in tpu_system_metadata.devices:
        if 'device:CPU:' in device.name and (master_job_name is None or
                                             master_job_name in device.name):
            self._hosts.append(device.name)
    self._num_cores_per_host = tpu_system_metadata.num_of_cores_per_host
    self._num_cores = tpu_system_metadata.num_cores

_validate_batch_size(self._batch_size, self._num_cores)
self._batch_size_per_core = self._batch_size // self._num_cores

# TODO(shizhiw): remove `mode`?
if mode == TRAINING:
    _validate_optimization_parameters(optimization_parameters,
                                      self._table_to_config_dict)
    self._optimization_parameters = optimization_parameters
elif mode == INFERENCE:
    if optimization_parameters is not None:
        raise ValueError(f'`optimization_parameters` should be `None` '
                         f'for inference mode. '
                         f'Received: {optimization_parameters}.')
    self._optimization_parameters = (StochasticGradientDescentParameters(1.))
else:
    raise ValueError('`mode` only supports {} and {}; got {}.'.format(
        TRAINING, INFERENCE, mode))
self._mode = mode

# TODO(shizhiw): move `optimization_parameters` into `_optimizer_handler`
# and create special handler for inference that inherits from
# StochasticGradientDescentHandler with more user-friendly error message
# on get_slot().
self._optimizer_handler_dict = self._get_optimizer_handler_by_table()

self._pipeline_execution_with_tensor_core = (
    pipeline_execution_with_tensor_core)
self._learning_rate_fn = list(
    set(c.learning_rate_fn
        for c in self._table_to_config_dict.values()
        if c.learning_rate_fn is not None))
self._learning_rate_fn_to_tag = {
    fn: id for id, fn in enumerate(self._learning_rate_fn)
}

self._config_proto = self._create_config_proto()
