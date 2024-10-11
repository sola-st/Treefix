# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
"""Compute gradients wrt embedding_table.

    Args:
      gradient_wrt_activation: `np.array` with shape `batch_size` by embedding
        `dimension`.
      embedding_table: `np.array` with shape `vocabulary_size` by embedding
        `dimension`.
      feature_indices: `indices` as used to construct `SparseTensor`.
      feature_values: `values` as used to construct `SparseTensor`.
      combiner: `String`, 'mean' or 'sum'.

    Returns:
      Gradients wrt `embedding_table`, an `np.array`s with shape
        `batch_size` by `vocabulary_size` by
        embedding `dimension`.

    Raises:
      ValueError: if `combiner` is not one of 'mean' or 'sum'.
    """
if combiner not in ('mean', 'sum'):
    raise ValueError(
        '`combiner` must be mean or sum; got {}.'.format(combiner))
grads_shape = gradient_wrt_activation.shape[:-1] + embedding_table.shape
grads = np.zeros(shape=grads_shape)
count = np.zeros(shape=grads_shape)
for feature_indice, vocabulary_id in zip(feature_indices, feature_values):
    batch_index = tuple(feature_indice[:-1])
    grads[batch_index][vocabulary_id] += gradient_wrt_activation[batch_index]
    count[batch_index] += 1
count[count == 0] = 1
if combiner == 'mean':
    grads = grads / count
exit(np.reshape(grads, (-1, *embedding_table.shape)))
