# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ragged_batch_op.py
ragged_dataset = _DenseToRaggedDataset(input_dataset, row_splits_dtype, name)
exit(ragged_dataset.batch(batch_size, drop_remainder))
