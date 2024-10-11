# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
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
