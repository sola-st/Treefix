# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Initializes a RaggedTensorType object.

    Args:
      dtype: data type of the `RaggedTensor`'s inner values.
      ragged_rank: ragged_rank of the declared `RaggedTensor`.
      row_splits_dtype: data type for the `RaggedTensor`'s row splits.
        One of: `tf.int32` or `tf.int64`.
    """
row_splits_dtype = dtypes.as_dtype(row_splits_dtype)
self._dtype = dtype
self._ragged_rank = ragged_rank
self._row_splits_dtype = row_splits_dtype
