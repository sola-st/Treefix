# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py

momenta_initializer = init_ops.zeros_initializer()
momenta_variables = _create_partitioned_variables(
    name=slot_variable_names.momenta,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=momenta_initializer)
slot_variables = MomentumSlotVariables(momenta_variables)

def load_ops_fn():
    """Returns the retrieve ops for Momentum embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    load_op_list = []
    config = config_proto
    for host_id, table_variable, momenta_variable in (zip(
        range(num_hosts), table_variables, momenta_variables)):
        with ops.colocate_with(table_variable):
            load_parameters_op = tpu_ops.load_tpu_embedding_momentum_parameters(
                parameters=table_variable,
                momenta=momenta_variable,
                table_name=table,
                num_shards=num_hosts,
                shard_id=host_id,
                config=config,
            )
        config = None
        load_op_list.append(load_parameters_op)
    exit(load_op_list)

def retrieve_ops_fn():
    """Returns the retrieve ops for Momentum embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    retrieve_op_list = []
    config = config_proto
    for host_id, table_variable, momenta_variable in (zip(
        range(num_hosts), table_variables, momenta_variables)):
        with ops.colocate_with(table_variable):
            retrieved_table, retrieved_momenta = (
                tpu_ops.retrieve_tpu_embedding_momentum_parameters(
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config,
                ))
            retrieve_parameters_op = control_flow_ops.group(
                state_ops.assign(table_variable, retrieved_table),
                state_ops.assign(momenta_variable, retrieved_momenta))
        config = None
        retrieve_op_list.append(retrieve_parameters_op)
    exit(retrieve_op_list)

exit((slot_variables, load_ops_fn, retrieve_ops_fn))
