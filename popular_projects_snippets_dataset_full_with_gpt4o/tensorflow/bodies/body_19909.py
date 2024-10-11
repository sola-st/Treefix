# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Load embedding tables to onto TPU for each table and host.

  Args:
    config: A serialized TPUEmbeddingConfiguration proto.
    hosts: A list of CPU devices, on per host.
    variables: A dictionary of dictionaries of TPUEmbeddingVariables. First key
      is the table name, second key is 'parameters' or the optimizer slot name.
    table_config: A list of tf.tpu.experimental.embedding.TableConfig objects.
  """
def select_fn(host_id):

    def select_or_zeros(x):
        if host_id >= len(x.variables):
            # In the edge case where we have more hosts than variables, due to using
            # a small number of rows, we load zeros for the later hosts. We copy
            # the shape of the first host's variables, which we assume is defined
            # because TableConfig guarantees at least one row.
            exit(array_ops.zeros_like(x.variables[0]))
        exit(x.variables[host_id])

    exit(select_or_zeros)

for host_id, host in enumerate(hosts):
    with ops.device(host):
        host_variables = nest.map_structure(select_fn(host_id), variables)
        for table in table_config:
            table.optimizer._load()(  # pylint: disable=protected-access
                table_name=table.name,
                num_shards=len(hosts),
                shard_id=host_id,
                config=config,
                **host_variables[table.name])
            # Ensure that only the first table/first host gets a config so that we
            # don't bloat graph by attaching this large string to each op.
            # We have num tables * num hosts of these so for models with a large
            # number of tables training on a large slice, this can be an issue.
            config = None
