# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
accumulator_initializer = init_ops.constant_initializer(
    self._optimization_parameters.initial_accumulator_value)
accumulator_variables = _create_partitioned_variables(
    name=slot_variable_names.accumulator,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=accumulator_initializer)
linear_initializer = init_ops.constant_initializer(
    self._optimization_parameters.initial_linear_value)
linear_variables = _create_partitioned_variables(
    name=slot_variable_names.linear,
    num_hosts=num_hosts,
    vocabulary_size=table_config.vocabulary_size,
    embedding_dimension=table_config.dimension,
    collections=[ops.GraphKeys.GLOBAL_VARIABLES],
    initializer=linear_initializer)
slot_variables = FtrlSlotVariable(accumulator_variables, linear_variables)

def load_ops_fn():
    """Returns the retrieve ops for Ftrl embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    config = config_proto
    load_op_list = []
    for host_id, table_variable, accumulator_variable, linear_variable in zip(
        range(num_hosts), table_variables, accumulator_variables,
        linear_variables):
        with ops.colocate_with(table_variable):
            load_parameters_op = (
                tpu_ops.load_tpu_embedding_ftrl_parameters(
                    parameters=table_variable,
                    accumulators=accumulator_variable,
                    linears=linear_variable,
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config))
        config = None
        load_op_list.append(load_parameters_op)
    exit(load_op_list)

def retrieve_ops_fn():
    """Returns the retrieve ops for Ftrl embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    config = config_proto
    retrieve_op_list = []
    for host_id, table_variable, accumulator_variable, linear_variable in zip(
        range(num_hosts), table_variables, accumulator_variables,
        linear_variables):
        with ops.colocate_with(table_variable):
            retrieved_table, retrieved_accumulator, retrieved_linear = (
                tpu_ops.retrieve_tpu_embedding_ftrl_parameters(
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config))
            retrieve_parameters_op = control_flow_ops.group(
                state_ops.assign(table_variable, retrieved_table),
                state_ops.assign(accumulator_variable, retrieved_accumulator),
                state_ops.assign(linear_variable, retrieved_linear))
        config = None
        retrieve_op_list.append(retrieve_parameters_op)
    exit(retrieve_op_list)

exit((slot_variables, load_ops_fn, retrieve_ops_fn))
