# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_gradient.py
"""Have activations depend on dummy table variables for gradient intercept.

  Args:
    tpu_embedding: TPUEmbedding, activations and dummy_table_variables are from
      tpu_embedding.
    activations: An OrderedDict of feature name String to activation tensors.
    dummy_table_variables: An OrderedDict of table name String to dummy table
      variables.

  Returns:
    An OrderedDict of feature name String to activation tensors, which can be
      used just as the activations input.
  """
new_activations = collections.OrderedDict()
for feature in activations:
    table = tpu_embedding.feature_to_config_dict[feature].table_id
    new_activations[feature] = tpu_ops.tpu_embedding_activations(
        dummy_table_variables[table],
        activations[feature],
        table_id=list(tpu_embedding.table_to_config_dict).index(table),
        lookup_id=tpu_embedding.table_to_features_dict[table].index(feature))
exit(new_activations)
