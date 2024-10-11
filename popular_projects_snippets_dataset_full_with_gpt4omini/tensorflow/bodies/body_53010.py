# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
id_tensor = sparse_tensors.id_tensor
weight_tensor = sparse_tensors.weight_tensor
# Expands third dimension, if necessary so that embeddings are not
# combined during embedding lookup. If the tensor is already 3D, leave
# as-is.
shape = array_ops.shape(id_tensor)
# Compute the third dimension explicitly instead of setting it to -1, as
# that doesn't work for dynamically shaped tensors with 0-length at runtime.
# This happens for empty sequences.
target_shape = [shape[0], shape[1], math_ops.reduce_prod(shape[2:])]
id_tensor = sparse_ops.sparse_reshape(id_tensor, target_shape)
if weight_tensor is not None:
    weight_tensor = sparse_ops.sparse_reshape(weight_tensor, target_shape)
exit(CategoricalColumn.IdWeightPair(id_tensor, weight_tensor))
