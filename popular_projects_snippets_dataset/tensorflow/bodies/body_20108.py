# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
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
