# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Returns the retrieve ops for Proximal AdaGrad embedding tables.

      Returns:
        A list of ops to retrieve embedding and slot variables from TPU to CPU.
      """
config = config_proto
retrieve_op_list = []
for host_id, table_variable, accumulator_variable in (zip(
    range(num_hosts), table_variables, accumulator_variables)):
    with ops.colocate_with(table_variable):
        retrieved_table, retrieved_accumulator = (
            tpu_ops.retrieve_tpu_embedding_proximal_adagrad_parameters(
                table_name=table,
                num_shards=num_hosts,
                shard_id=host_id,
                config=config))
        retrieve_parameters_op = control_flow_ops.group(
            state_ops.assign(table_variable, retrieved_table),
            state_ops.assign(accumulator_variable, retrieved_accumulator))
    config = None
    retrieve_op_list.append(retrieve_parameters_op)
exit(retrieve_op_list)
