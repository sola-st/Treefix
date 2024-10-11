# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Retrieve embedding tables from TPU to host memory.

  Args:
    config: A serialized TPUEmbeddingConfiguration proto.
    hosts: A list of all the host CPU devices.
    variables: A dictionary of dictionaries of TPUEmbeddingVariables. First key
      is the table name, second key is 'parameters' or the optimizer slot name.
    table_config: A list of tf.tpu.experimental.embedding.TableConfig objects.
  """
for host_id, host in enumerate(hosts):
    with ops.device(host):
        for table in table_config:
            retrieved = table.optimizer._retrieve()(  # pylint: disable=protected-access
                table_name=table.name,
                num_shards=len(hosts),
                shard_id=host_id,
                config=config)
            # When there are no slot variables (e.g with SGD) this returns a
            # single tensor rather than a tuple. In this case we put the tensor in
            # a list to make the following code easier to write.
            if not isinstance(retrieved, tuple):
                retrieved = (retrieved,)

            for i, slot in enumerate(["parameters"] +
                                     table.optimizer._slot_names()):  # pylint: disable=protected-access
                # We must assign the CPU variables the values of tensors that were
                # returned from the TPU.
                sharded_var = variables[table.name][slot]
                if host_id < len(sharded_var.variables):
                    # In the edge case where we have more hosts than variables, due to
                    # using a small number of rows, we skip the later hosts.
                    sharded_var.variables[host_id].assign(retrieved[i])
        # Ensure that only the first table/first host gets a config so that we
        # don't bloat graph by attaching this large string to each op.
        # We have num tables * num hosts of these so for models with a large
        # number of tables training on a large slice, this can be an issue.
            config = None
