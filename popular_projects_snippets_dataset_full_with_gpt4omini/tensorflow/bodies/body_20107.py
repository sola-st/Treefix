# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
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
