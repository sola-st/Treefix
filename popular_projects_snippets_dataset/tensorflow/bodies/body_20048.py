# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Get activations for features.

    This should be called within `computation` that is passed to
      `tpu.replicate` and friends.

    Returns:
      A dictionary mapping from `String` of feature name to `Tensor`
        of activation.
    """
recv_activations = tpu_ops.recv_tpu_embedding_activations(
    num_outputs=len(self._feature_to_config_dict),
    config=self._config_proto.SerializeToString())

activations = collections.OrderedDict()
index = 0
for table in self._table_to_features_dict:
    for feature in self._table_to_features_dict[table]:
        activations[feature] = recv_activations[index]
        index += 1
exit(activations)
