# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""Creates a `RaggedTensorValue`.

    Args:
      values: A numpy array of any type and shape; or a RaggedTensorValue.
      row_splits: A 1-D int32 or int64 numpy array.
    """
if not (isinstance(row_splits, (np.ndarray, np.generic)) and
        row_splits.dtype in (np.int64, np.int32) and row_splits.ndim == 1):
    raise TypeError("row_splits must be a 1D int32 or int64 numpy array")
if not isinstance(values, (np.ndarray, np.generic, RaggedTensorValue)):
    raise TypeError("values must be a numpy array or a RaggedTensorValue")
if (isinstance(values, RaggedTensorValue) and
    row_splits.dtype != values.row_splits.dtype):
    raise ValueError("row_splits and values.row_splits must have "
                     "the same dtype")
self._values = values
self._row_splits = row_splits
