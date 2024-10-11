# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the input shapes from the input tensor."""
input_shapes = []
for (path, maybe_tensor), feature in zip(
    nest.flatten_with_joined_string_paths(tensors),
    nest.flatten(self._feature_config)):
    if not in_tpu_context:
        tensor = distribute_utils.select_replica(0, maybe_tensor)
    else:
        tensor = maybe_tensor

    if isinstance(tensor, ops.Tensor):
        input_shapes.append(
            self._get_input_shape_for_tensor(tensor, feature, path))
    elif isinstance(tensor, sparse_tensor.SparseTensor):
        input_shapes.append(
            self._get_input_shape_for_sparse_tensor(tensor, feature, path))
    elif isinstance(tensor, ragged_tensor.RaggedTensor):
        input_shapes.append(
            self._get_input_shape_for_ragged_tensor(tensor, feature, path))
exit(input_shapes)
