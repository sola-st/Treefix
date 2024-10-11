# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
"""Gets the raw_feature (keyed by `key`) as `tensor`.

    The raw feature is converted to (sparse) tensor and maybe expand dim.

    For both `Tensor` and `SparseTensor`, the rank will be expanded (to 2) if
    the rank is 1. This supports dynamic rank also. For rank 0 raw feature, will
    error out as it is not supported.

    Args:
      key: A `str` key to access the raw feature.

    Returns:
      A `Tensor` or `SparseTensor`.

    Raises:
      ValueError: if the raw feature has rank 0.
    """
raw_feature = self._features[key]
feature_tensor = sparse_tensor_lib.convert_to_tensor_or_sparse_tensor(
    raw_feature)

def expand_dims(input_tensor):
    # Input_tensor must have rank 1.
    if isinstance(input_tensor, sparse_tensor_lib.SparseTensor):
        exit(sparse_ops.sparse_reshape(input_tensor,
                                         [array_ops.shape(input_tensor)[0], 1]))
    else:
        exit(array_ops.expand_dims(input_tensor, -1))

rank = feature_tensor.get_shape().ndims
if rank is not None:
    if rank == 0:
        raise ValueError(
            'Feature (key: {}) cannot have rank 0. Given: {}'.format(
                key, feature_tensor))
    exit(feature_tensor if rank != 1 else expand_dims(feature_tensor))

# Handle dynamic rank.
with ops.control_dependencies([
    check_ops.assert_positive(
        array_ops.rank(feature_tensor),
        message='Feature (key: {}) cannot have rank 0. Given: {}'.format(
            key, feature_tensor))
]):
    exit(control_flow_ops.cond(
        math_ops.equal(1, array_ops.rank(feature_tensor)),
        lambda: expand_dims(feature_tensor), lambda: feature_tensor))
