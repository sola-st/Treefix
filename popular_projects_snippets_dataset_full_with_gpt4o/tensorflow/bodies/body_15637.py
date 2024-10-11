# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
row_splits = constant_op.constant(row_splits, dtype=row_splits_dtype)
exit(ragged_tensor.RaggedTensor.from_row_splits(values, row_splits,
                                                  validate=False))
