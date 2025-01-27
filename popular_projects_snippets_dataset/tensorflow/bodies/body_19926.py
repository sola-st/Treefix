# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Apply embedding lookup on TPUs using Tensorcore.

    Note that all the sparse and ragged tensors will be converted to dense
    tensors on CPU and then passed to the TPU to do embedding look up. Large
    embedding lookup is not supported by this API, use the TPUEmbedding mid
    level api instead.

    Args:
      features: a nested structure of Tensors, SparseTensors or RaggedTensors.
      weights: a nested structure of Tensors, SparseTensors or RaggedTensors or
        None for no weights. If not None, structure must match that of inputs,
        but entries are allowed to be None.

    Returns:
      A nested structure of Tensors with the same structure as inputs.
    """
if not self._built:
    self.build()
nest.assert_same_structure(features, self._feature_config)

flat_inputs = nest.flatten(features)
flat_weights = [None] * len(flat_inputs)
if weights is not None:
    nest.assert_same_structure(features, weights)
    flat_weights = nest.flatten(weights)
flat_features = nest.flatten_with_joined_string_paths(self._feature_config)

outputs = []
for inp, weight, (path, feature) in zip(flat_inputs, flat_weights,
                                        flat_features):
    table = self.embedding_tables[feature.table]

    if weight is not None:
        if isinstance(inp, ops.Tensor):
            raise ValueError(
                "Weight specified for {}, but input is dense.".format(path))
        elif type(weight) is not type(inp):
            raise ValueError(
                "Weight for {} is of type {} but it does not match type of the "
                "input which is {}.".format(path, type(weight), type(inp)))
        elif feature.max_sequence_length > 0:
            raise ValueError("Weight specified for {}, but this is a sequence "
                             "feature.".format(path))

    if isinstance(inp, ops.Tensor):
        if feature.max_sequence_length > 0:
            raise ValueError(
                "Feature {} is a sequence feature but a dense tensor "
                "was passed.".format(path))
        outputs.append(embedding_ops.embedding_lookup_v2(table, inp))

    elif isinstance(inp, sparse_tensor.SparseTensor):
        outputs.append(
            self._embedding_lookup_for_sparse_tensor(inp, weight, table,
                                                     feature))
    elif isinstance(inp, ragged_tensor.RaggedTensor):
        outputs.append(
            self._embedding_lookup_for_ragged_tensor(inp, weight, table,
                                                     feature))
    else:
        raise ValueError("Input {} is type {}. Tensor, SparseTensor or "
                         "RaggedTensor expected.".format(path, type(inp)))
exit(nest.pack_sequence_as(self._feature_config, outputs))
