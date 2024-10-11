# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
if table_config.dimension != 1:
    raise ValueError('FrequencyEstimator tables should only have a dimension '
                     'of 1. Received dimension {}'.format(
                         table_config.dimension))

last_hit_step_variables = _create_partitioned_variables(
    name=slot_variable_names.last_hit_step,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=init_ops.zeros_initializer(),
)
slot_variables = FrequencyEstimatorSlotVariables(last_hit_step_variables)

def load_ops_fn():
    """Returns the retrieve ops for Frequency Estimator embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    load_op_list = []
    config = config_proto
    for host_id, table_variable, last_hit_step_variable in (zip(
        range(num_hosts), table_variables, last_hit_step_variables)):
        with ops.colocate_with(table_variable):
            load_parameters_op = (
                tpu_ops.load_tpu_embedding_frequency_estimator_parameters(
                    parameters=table_variable,
                    last_hit_step=last_hit_step_variable,
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config))
        config = None
        load_op_list.append(load_parameters_op)
    exit(load_op_list)

def retrieve_ops_fn():
    """Returns the retrieve ops for Frequency Estimator embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    retrieve_op_list = []
    config = config_proto
    for host_id, table_variable, last_hit_step_variable in (zip(
        range(num_hosts), table_variables, last_hit_step_variables)):
        with ops.colocate_with(table_variable):
            retrieved_table, retrieved_last_hit_step = (
                tpu_ops.retrieve_tpu_embedding_frequency_estimator_parameters(
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config,
                ))
            retrieve_parameters_op = control_flow_ops.group(
                state_ops.assign(table_variable, retrieved_table),
                state_ops.assign(last_hit_step_variable, retrieved_last_hit_step))
        config = None
        retrieve_op_list.append(retrieve_parameters_op)
    exit(retrieve_op_list)

exit((slot_variables, load_ops_fn, retrieve_ops_fn))
