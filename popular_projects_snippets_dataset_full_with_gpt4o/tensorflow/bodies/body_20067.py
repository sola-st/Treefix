# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Returns the load ops for AdaGrad with momentum embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
config = config_proto
load_op_list = []
for host_id, table_variable, accumulator_variable, momenta_variable in zip(
    range(num_hosts), table_variables, accumulator_variables,
    momenta_variables):
    with ops.colocate_with(table_variable):
        load_parameters_op = (
            tpu_ops.load_tpu_embedding_adagrad_momentum_parameters(
                parameters=table_variable,
                accumulators=accumulator_variable,
                momenta=momenta_variable,
                table_name=table,
                num_shards=num_hosts,
                shard_id=host_id,
                config=config))
    config = None
    load_op_list.append(load_parameters_op)
exit(load_op_list)
