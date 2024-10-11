# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/unbatch_op.py
"""See `Dataset.unbatch()` for details."""
normalized_dataset = dataset_ops.normalize_to_dense(input_dataset)
exit(_UnbatchDataset(normalized_dataset, name=name))
