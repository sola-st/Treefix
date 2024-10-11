# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Returns the load ops for Proximal Yogi embedding tables.

      Returns:
        A list of ops to load embedding and slot variables from CPU to TPU.
      """
load_op_list = []
config = config_proto
for host_id, table_variable, v_variable, m_variable in (zip(
    range(num_hosts), table_variables, v_variables, m_variables)):
    with ops.colocate_with(table_variable):
        load_parameters_op = (
            tpu_ops.load_tpu_embedding_proximal_yogi_parameters(
                parameters=table_variable,
                v=v_variable,
                m=m_variable,
                table_name=table,
                num_shards=num_hosts,
                shard_id=host_id,
                config=config))
    # Set config to None to enforce that config is only loaded to the first
    # table.
    config = None
    load_op_list.append(load_parameters_op)
exit(load_op_list)
