# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
del table_config

def load_ops_fn():
    """Returns the retrieve ops for AdaGrad embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
    load_op_list = []
    config = config_proto
    for host_id, table_variable in enumerate(table_variables):
        with ops.colocate_with(table_variable):
            load_parameters_op = (
                tpu_ops.load_tpu_embedding_stochastic_gradient_descent_parameters(
                    parameters=table_variable,
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config))
        config = None
        load_op_list.append(load_parameters_op)
    exit(load_op_list)

def retrieve_ops_fn():
    """Returns the retrieve ops for SGD embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
    retrieve_op_list = []
    config = config_proto
    for host_id, table_variable in enumerate(table_variables):
        with ops.colocate_with(table_variable):
            retrieved_table = (
                tpu_ops
                .retrieve_tpu_embedding_stochastic_gradient_descent_parameters(
                    table_name=table,
                    num_shards=num_hosts,
                    shard_id=host_id,
                    config=config))
            retrieve_parameters_op = control_flow_ops.group(
                state_ops.assign(table_variable, retrieved_table))
        config = None
        retrieve_op_list.append(retrieve_parameters_op)
    exit(retrieve_op_list)

exit((None, load_ops_fn, retrieve_ops_fn))
