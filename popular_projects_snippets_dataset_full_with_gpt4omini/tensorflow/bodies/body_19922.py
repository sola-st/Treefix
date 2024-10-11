# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Create variables for TPU embeddings.

    Note that this will always ensure that the variable is created under the
    TPUStrategy.

    Returns:
      A dict of dicts. The outer dict is keyed by the table names and the inner
      dicts are keyed by 'parameters' and the slot variable names.
    """
variables = {}
for table in self._table_config:
    # created TPUDistributedVariable.
    variables[table.name] = self._create_variables(table, trainable=True)
exit(variables)
