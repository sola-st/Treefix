# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py

ms_variables = _create_partitioned_variables(
    name=slot_variable_names.ms,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=init_ops.zeros_initializer(),
)
mom_variables = _create_partitioned_variables(
    name=slot_variable_names.mom,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=init_ops.zeros_initializer(),
)
slot_variables = RMSPropSlotVariables(ms_variables, mom_variables)

def load_ops_fn():
    """Returns the retrieve ops for RMS Prop embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    load_op_list = []
    config = config_proto
    for host_id, table_variable, ms_variable, mom_variable in (zip(
        range(num_hosts), table_variables, ms_variables, mom_variables)):
        with ops.colocate_with(table_variable):
            load_parameters_op = tpu_ops.load_tpu_embedding_rms_prop_parameters(
                parameters=table_variable,
                ms=ms_variable,
                mom=mom_variable,
                table_name=table,
                num_shards=num_hosts,
                shard_id=host_id,
                config=config,
            )
        config = None
        load_op_list.append(load_parameters_op)
    exit(load_op_list)

def retrieve_ops_fn():
    """Returns the retrieve ops for RMS Prop embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    retrieve_op_list = []
    config = config_proto
    for host_id, table_variable, ms_variable, mom_variable in (zip(
        range(num_hosts), table_variables, ms_variables, mom_variables)):
        with ops.colocate_with(table_variable):
            retrieved_table, retrieved_ms, retrieved_mom = (
                tpu_ops.retrieve_tpu_embedding_rms_prop_parameters(
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config,
                ))
            retrieve_parameters_op = control_flow_ops.group(
                state_ops.assign(table_variable, retrieved_table),
                state_ops.assign(ms_variable, retrieved_ms),
                state_ops.assign(mom_variable, retrieved_mom))
        config = None
        retrieve_op_list.append(retrieve_parameters_op)
    exit(retrieve_op_list)

exit((slot_variables, load_ops_fn, retrieve_ops_fn))
