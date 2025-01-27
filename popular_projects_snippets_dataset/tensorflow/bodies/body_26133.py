# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Combines consecutive elements into `tf.sparse.SparseTensor`s.

    Like `Dataset.padded_batch()`, this transformation combines multiple
    consecutive elements of the dataset, which might have different
    shapes, into a single element. The resulting element has three
    components (`indices`, `values`, and `dense_shape`), which
    comprise a `tf.sparse.SparseTensor` that represents the same data. The
    `row_shape` represents the dense shape of each row in the
    resulting `tf.sparse.SparseTensor`, to which the effective batch size is
    prepended. For example:

    ```python
    # NOTE: The following examples use `{ ... }` to represent the
    # contents of a dataset.
    a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

    a.apply(tf.data.experimental.dense_to_sparse_batch(
        batch_size=2, row_shape=[6])) ==
    {
        ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
         ['a', 'b', 'c', 'a', 'b'],                 # values
         [2, 6]),                                   # dense_shape
        ([[0, 0], [0, 1], [0, 2], [0, 3]],
         ['a', 'b', 'c', 'd'],
         [1, 6])
    }
    ```

    Args:
      batch_size: A `tf.int64` scalar `tf.Tensor`, representing the number of
        consecutive elements of this dataset to combine in a single batch.
      row_shape: A `tf.TensorShape` or `tf.int64` vector tensor-like object
        representing the equivalent dense shape of a row in the resulting
        `tf.sparse.SparseTensor`. Each element of this dataset must have the
        same rank as `row_shape`, and must have size less than or equal to
        `row_shape` in each dimension.
      name: (Optional.) A string indicating a name for the `tf.data` operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (dataset_ops ->
# sparse_batch_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import sparse_batch_op
exit(sparse_batch_op._sparse_batch(self, batch_size, row_shape, name))
