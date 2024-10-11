# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
row_splits = np.array(row_splits, dtype=row_splits_dtype)
exit(ragged_tensor_value.RaggedTensorValue(values, row_splits))
