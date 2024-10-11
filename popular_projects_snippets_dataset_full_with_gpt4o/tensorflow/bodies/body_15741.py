# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_one_hot_op_test.py
"""Tests that tf.one_hot gives the same result for ragged & uniform tensors.

    Runs tf.one_hot with a uniform tensor, and compares the output with the
    results of calling tf.one_hot with ragged version of that tensor with
    varying ragged ranks.

    Args:
      indices_shape: Shape for `indices` arg to `tf.one_hot`
      depth: `depth` arg to `tf.one_hot`
      on_value: `on_value` arg to `tf.one_hot`
      off_value: `off_value` arg to `tf.one_hot`
      axis: `axis` arg to `tf.one_hot`
      dtype: `dtype` arg to `tf.one_hot`
    """
indices_shape = tensor_shape.as_shape(indices_shape)
indices = np.random.randint(depth + 1, size=indices_shape)
expected = array_ops.one_hot(
    indices,
    depth,
    on_value=on_value,
    off_value=off_value,
    axis=axis,
    dtype=dtype)
for ragged_rank in range(1, len(indices_shape)):
    if axis is not None and 0 <= axis <= ragged_rank:
        continue  # axis <= ragged_rank is not supported.
    ragged_indices = ragged_tensor.RaggedTensor.from_tensor(
        indices, ragged_rank=ragged_rank)
    result = ragged_array_ops.ragged_one_hot(
        ragged_indices,
        depth,
        on_value=on_value,
        off_value=off_value,
        axis=axis,
        dtype=dtype)
    self.assertAllEqual(result.to_tensor(), expected)
